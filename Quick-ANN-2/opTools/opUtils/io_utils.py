import os;
import yaml;
import pandas as pd;
import logging;
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_BZIP2, ZIP_LZMA;
from keras import models;

log = logging.getLogger(__name__);


def archive_df_csv(target_archive:ZipFile, filename:str|os.PathLike, df:pd.DataFrame, **write_csv_opts) -> None:
    log.debug("saving via the '.csv' method");
    with target_archive.open(filename, "w") as target_file:
        df.to_csv(target_file, *write_csv_opts);
    
def archive_ann(target_archive:ZipFile, filename:str|os.PathLike, trained_ann:models.Model, tmp_path:os.PathLike=os.path.join(".", "DATA") , **write_model_opts) -> None:
    log.debug("saving via the '.keras' method");
    tmp_file = str(os.path.join(tmp_path, filename));
    models.save_model(trained_ann, tmp_file, overwrite=True);
    try:
        target_archive.write(tmp_file, filename);
    finally:
        os.remove(tmp_file);
    
DATA_EXPORTERS = {
    ".csv" : archive_df_csv,
    ".keras": archive_ann,
    };


def extract_df_csv(source_archive: ZipFile, filename:str, **df_extract_args):
    df = None;
    with source_archive.open(filename) as zipped_file:
        df = pd.read_csv(zipped_file, **df_extract_args);
    return df;
    
def extract_ann_model(source_archive: ZipFile, filename:str, **ann_extract_args):
    path, _ = os.path.split(source_archive.filename); 
    source_archive.extract(filename, path);
    filepath = os.path.join(path, filename);
    model = models.load_model(filepath);
    os.remove(filepath);
    return model;
    
DATA_EXTRACTORS = {
    ".csv" : extract_df_csv,
    ".keras": extract_ann_model,
}

def load_configuration(config_file_path):
    with open(config_file_path, 'r') as f_stream:
        config = yaml.safe_load(f_stream);    
    if config["version"] == 1.0:
        config["scenario"] = list(((command, params) for step in config["scenario"] for command, params in step.items() ));
    return config;


def dfs_from_zip(files_names:list, archive_file_name:str|os.PathLike, data_path = ['.', 'data'], **read_csv_options):
    file = os.path.join(*data_path, archive_file_name);
    log.info(f"Extract the '{", ".join(files_names)}' files data from the '{file}' ZIP archive.");
    dfs = [];
    with ZipFile(file) as zip:
        log.debug(f"The archive consists of: {[z.filename for z in zip.infolist()]}");
        for file_name in files_names:
            df = DATA_EXTRACTORS[os.path.splitext(file_name)[1]](zip, file_name, **read_csv_options);
            dfs.append(df);
    return dfs;


def dfs_to_zip(dfs:list, filenames:list, archive_file_name:str|os.PathLike, archive_path = ['.', 'DATA'], mode="w", **write_csv_options):
    file = os.path.join(*archive_path, archive_file_name);
    log.info(f"Archive the '{", ".join(filenames)}' files data to the '{file}' ZIP archive.");
    with ZipFile(file, mode, compression=ZIP_BZIP2) as archive:
        for file_name, df in zip(filenames, dfs):
            log.info(f"Exporting the {file_name}");
            DATA_EXPORTERS[os.path.splitext(file_name)[1]](archive, file_name, df, **write_csv_options);
           
    return None;
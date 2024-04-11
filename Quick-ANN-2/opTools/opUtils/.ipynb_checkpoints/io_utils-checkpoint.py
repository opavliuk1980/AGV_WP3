import os;
import yaml;
import pandas as pd;
import logging;
from zipfile import ZipFile;

log = logging.getLogger(__name__);

def load_configuration(config_file_path):
    with open(config_file_path, 'r') as f_stream:
        config = yaml.safe_load(f_stream);
    
    if config["version"] == 1.0:
        config["scenario"] = list(((command, params) for step in config["scenario"] for command, params in step.items() ));
    
    return config;
    
def df_from_csv(file_name, data_path = ['.', 'data'], archive_file_name=None, delimiter = ","):
    file = os.path.join(*data_path, archive_file_name or file_name);
    
    log.info(f"Load csv data from the {file} ...")    
    if not archive_file_name:
        return pd.read_csv(file, delimiter=delimiter, index_col=False, low_memory=False);

    log.info(f"Extract the '{file_name}' file from ZIP archive.");
    df = None;
    with ZipFile(file) as zip:
        log.debug(f"Arcive consists of: {[z.filename for z in zip.infolist()]}");
        with zip.open(file_name) as zipped_file:    
            df = pd.read_csv(zipped_file, delimiter=delimiter, index_col=False, low_memory=False);
    return df;
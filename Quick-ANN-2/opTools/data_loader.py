import opTools.opUtils.io_utils as opio;
import logging;
log = logging.getLogger(__name__);

def execute(df, files_names, data_path=["."], archive_file_name=None, **kwargs):
    if(len(files_names) == 0):
        return [opio.df_from_csv(files_names[0], data_path, archive_file_name, **kwargs)];
    return opio.dfs_from_zip(files_names, archive_file_name, data_path, **kwargs);

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG");    

    log.info("Start loading ...")
    df = execute(None, ["6000_frames_20221124+25_new.pkl", "6000_frames_20221124+25_new.pkl"], [".", "DATA"], 
                 archive_file_name="6000_frame.zip",
                 low_memory=False, index_col=False, delimiter=",");
    log.info(f"Loaded --\n{df}");
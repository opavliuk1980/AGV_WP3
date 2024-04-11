import opTools.opUtils.io_utils as opio;
import logging;
log = logging.getLogger(__name__);

def execute(df, file_name, data_path=["."], archive_file_name=None, **kwargs):
    return opio.df_from_csv(file_name, data_path, archive_file_name, **kwargs);

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG");    

    log.info("Start loading ...")
    df = execute(None, "6000_frames_20221124+25_new.pkl", [".", "DATA"], archive_file_name="6000_frame.zip" );
    log.info(f"Loaded --\n{df}");
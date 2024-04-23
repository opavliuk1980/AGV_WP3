import os;
import opTools.opUtils.io_utils as opio;
import logging;
log = logging.getLogger(__name__);


def execute(dfs:list, filenames:list, archive_file_name:str|os.PathLike, archive_path = ['.', 'data'], **write_csv_options):
    opio.dfs_to_zip(dfs, filenames, archive_file_name, archive_path, mode="w", **write_csv_options);
    return None;
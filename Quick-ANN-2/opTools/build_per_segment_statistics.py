from opTools.opUtils.data_preprocessing import collect_segments_statistics, group_collect_statistics

def execute(dfs_list_grouped, datetime_format):
    dfs_list, dfs_grouped = dfs_list_grouped;
    df_segments_route = collect_segments_statistics(dfs_list, format = datetime_format);
    df_segments_dictionary = group_collect_statistics(dfs_grouped, format = datetime_format);
    return (df_segments_route, df_segments_dictionary)

    
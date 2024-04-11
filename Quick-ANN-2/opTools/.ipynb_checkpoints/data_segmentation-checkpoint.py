def segment_data_by(df, segmentation_column:str):
    col_data = df[segmentation_column];
    col_data.index = list(range(col_data.shape[0]));
   
    route_segments = col_data[(col_data != col_data.shift(1))];
    segments_indexes = route_segments.index.values;
    segments_intervals = zip(segments_indexes[:-1], segments_indexes[1:]);
    dfs = [(f,t, col_data[f], df[f:t]) for f,t in segments_intervals];
    
    last = segments_indexes[-1];
    dfs.append((last, None, col_data[last], df[last:]));
    return dfs;


def segments_route(dfs:list) -> list:
    return [df for f, t, segment, df in dfs];


def group_segments(dfs:list) -> dict :
    gdfs = {};
    for f, t, segment, df in dfs:
        segment_data = gdfs.get(segment, []);
        segment_data.append(df);
        gdfs.update({segment:segment_data});
    return gdfs;


def execute(df, segmentation_column:str, ignore_segments:list=None):
    df_source = df[~df[segmentation_column].isin(ignore_segments)];
    dfs = segment_data_by(df_source, segmentation_column);
    dfs_list = segments_route(dfs);
    dfs_grouped = group_segments(dfs);
    return (dfs_list, dfs_grouped)
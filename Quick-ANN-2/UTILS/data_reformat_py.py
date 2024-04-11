import pandas as pd
import math
from functools import reduce;



def segment_changes(df, column_name:str):
    def append_list(l, v):
        if len(l) == 0 or l[-1][1] != v[1]: l.append(v);
        return l;

    segments_samples = df[column_name].array;
    return reduce(append_list, list(enumerate(segments_samples)), []);

def split_data_by(df, column_name:str, dfs:list,  label = ""):
    seg_changes = segment_changes(df, column_name);
    start_seg, cur_seg = seg_changes[0];
    n = 0;
    for end_seg, new_seg in seg_changes[1:]:
        new_df = df[start_seg:end_seg];
        n += 1;
        dfs.append(new_df)
        cur_seg, start_seg = new_seg, end_seg;
    return dfs;

def group_data_by(df, column_name:str, dfs:dict,  label:str = ""):
    seg_changes = segment_changes(df, column_name);
    start_seg, cur_seg = seg_changes[0];
    n = 0;
    for end_seg, new_seg in seg_changes[1:]:
        seg_key = "".join(['seg'+str(cur_seg), label]);
        new_df = df[start_seg:end_seg];
        n += 1;
        if seg_key in dfs.keys():
            dfs[seg_key].append(new_df);
        else:
            dfs[seg_key] = [new_df,];
        cur_seg, start_seg = new_seg, end_seg;
    return dfs;
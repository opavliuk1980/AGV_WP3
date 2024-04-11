def execute(
    df, 
    valid_data_range:list=None, 
    processing_columns:list=None, 
    aggregated_columns:dict=None,
    rename_columns:dict=None,
    index:str=None
):
    d_from, d_to = valid_data_range if valid_data_range else [0, -1];
    columns = processing_columns if processing_columns else df.columns
    
    df_source = df.loc[d_from:d_to, columns];
    if aggregated_columns:
        for col_name, cols in aggregated_columns.items():
            df_source[col_name] = df.loc[d_from:d_to, cols].sum(axis=1);

    if rename_columns:
        df_source.rename(columns = rename_columns, inplace = True);
        
    df_source.index = df.loc[d_from:d_to, index] if index else df.index[d_from:d_to+1];
    return df_source


if __name__ == "__main__":
    import pandas as pd;
    import sys;

    print("Data re-format demo:")
    df = pd.DataFrame({
        "id":[12,13,14],
        "first name":["Vita", "Sasha", "Grisha"], 
        "Last name": ["Byork", "Giga", "Ohayo"],
        "Age":[20, 21, 19], "Sex":["F", "M", "F"], 
        "salary": [1000, 1100, 950], "tax":[-20, -25, -18]}
    );
    print(f"Origin data:\n{str(df)}");

    df1 = execute(
        df, 
        valid_data_range = [1, 3], 
        processing_columns = ["first name", "Last name", "salary", "tax"], 
        aggregated_columns = {"total": ["salary", "tax"]},
        rename_columns = {"Last name": "last name"},
        index = "id"
    );
    print(f"\nRe-formated data:\n{df1}");

    sys.exit(0);
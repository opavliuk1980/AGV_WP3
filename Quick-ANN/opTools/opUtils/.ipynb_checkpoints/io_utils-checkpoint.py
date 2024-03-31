import os;
import yaml;
import pandas as pd;

def load_configuration(config_file_path):
    with open(config_file_path, 'r') as f_stream:
        config = yaml.safe_load(f_stream)
    return config;
    
def df_from_csv(file_name, data_path = ['.', 'data'], delimiter = ","):
    file_path = os.path.join(*data_path, file_name);
    return pd.read_csv(file_path, delimiter=delimiter, index_col=False, low_memory=False);

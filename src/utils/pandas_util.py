import pandas as pd
import tarfile

def load_data_frame_from_csv_file(path):
    return pd.read_csv(path)

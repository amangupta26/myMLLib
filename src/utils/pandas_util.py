import pandas as pd
from sklearn.model_selection import train_test_split

def load_data_frame_from_csv_file(path):
    return pd.read_csv(path)

def get_training_data_label_by_label_columns(data_frame, label_columns):
    y = data_frame[label_columns]
    X = data_frame.drop(columns=label_columns)
    return X, y


def split_data_frame_train_test(X, y, test_size=0.25):
    return train_test_split(X, y, test_size=test_size)





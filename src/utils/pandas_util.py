import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit

def load_data_frame_from_csv_file(path):
    return pd.read_csv(path)

def get_training_data_label_by_label_columns(data_frame, label_columns):
    y = data_frame[label_columns]
    X = data_frame.drop(columns=label_columns)
    return X, y


def random_split_data_frame_train_test_label(X, y, test_size=0.25, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def stratified_shuffle_split_data_frame_train_test(X, y, test_size=0.25, n_splits=1, random_state=42):
    stratified_shuffle_split = StratifiedShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=random_state)

    for train_index, test_index in stratified_shuffle_split.split(X, y):
        X_train = X.loc[train_index]
        X_test = X.loc[test_index]
    return X_train, X_test








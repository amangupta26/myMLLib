import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit


def load_data_frame_from_csv_file(path):
    return pd.read_csv(path)


def get_training_data_label_by_label_columns(data_frame, label_columns):
    label_vector = data_frame[label_columns]
    training_data = data_frame.drop(columns=label_columns)
    return training_data, label_vector


def random_split_data_frame_train_test_label(X, y, test_size=0.25, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def stratified_shuffle_split_data_frame_train_test(data_frame, split_column_name, test_size=0.25, n_splits=1, random_state=42):
    stratified_shuffle_split = StratifiedShuffleSplit(n_splits=n_splits, test_size=test_size, random_state=random_state)

    for train_index, test_index in stratified_shuffle_split.split(data_frame, data_frame[split_column_name]):
        data_frame_train = data_frame.loc[train_index]
        data_frame_test = data_frame.loc[test_index]
    return data_frame_train, data_frame_test


def filter_data_frame_by_columns(data_frame, label_columns):
    return data_frame[label_columns]


def get_nan_columns_map(data_frame):
    nan_column_map = {}
    temp_series = data_frame.isnull().sum()
    for column_name, nan_count in temp_series.items():
        if nan_count > 0:
            nan_column_map[column_name] = nan_count
    return nan_column_map


# Returns rows which are NaN in data frame
def get_nan_rows(data_frame):
    return data_frame[data_frame.isnull().T.any().T]


def get_data_frame_column_names_by_list(data_frame):
    return list(data_frame.columns)








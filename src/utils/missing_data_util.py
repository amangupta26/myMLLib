from sklearn.preprocessing import Imputer
import pandas as pd


def drop_na_rows(data_frame, columns):
    return data_frame.dropna(subset=columns)


def drop_column(data_frame, column):
    return data_frame.drop(column, axis=1)


def fill_na(data_frame, column, with_value):
    return data_frame[column].fillna(with_value)


def apply_imputer_on_numerical_data(data_frame, strategy="median"):
    imputer = Imputer(strategy=strategy)
    imputer.fit(data_frame)
    X = imputer.transform(data_frame)
    return pd.DataFrame(X, columns=data_frame.columns), imputer
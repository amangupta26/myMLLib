from sklearn.preprocessing import OneHotEncoder


def one_hot_encode_single_column(data_frame, column_name, sparse=False):
    encoder = OneHotEncoder(sparse=sparse)
    temp_one_hot = encoder.fit_transform(data_frame[column_name].values.reshape(-1,1))
    return temp_one_hot
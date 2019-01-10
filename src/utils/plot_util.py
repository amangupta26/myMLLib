import matplotlib.pyplot as plt

def plot_all_features_of_pandas_data_frame(df, bins=50, figsize=(20,15)):
    df.hist(bins=bins, figsize=figsize)
    plt.show()
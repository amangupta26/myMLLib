import matplotlib.pyplot as plt

def plot_all_features_of_pandas_data_frame(data_frame, bins=50, figsize=(20, 15)):
    data_frame.hist(bins=bins, figsize=figsize)
    plt.show()

def plot_scatter(data_frame, x_axis_colimn_name, y_axis_colimn_name, alpha=0.1):
    data_frame.plot(kind="scatter", x=x_axis_colimn_name, y=y_axis_colimn_name, alpha=alpha)
    plt.show()
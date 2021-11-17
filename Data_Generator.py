import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas import DataFrame
import more_itertools
import seaborn as sns
import plotly
from sklearn.datasets import make_classification


# parameters to vary n_clusters_per_class int(1 or 2), class_seperation int(0-10), weights [(0-1),(0-1)], flip_y (0-1)

def generate_data(n_samples, cluster_per_c, class_sep, noise, weight_c1):
    weight_c2=1-weight_c1
    X, y = make_classification(n_samples=n_samples, n_features=2, n_informative=2, n_redundant=0, n_repeated=0, n_classes=2,
                               n_clusters_per_class=cluster_per_c, class_sep=class_sep, flip_y=noise,
                               weights=[weight_c1, weight_c2], random_state=15)
    return X, y


# # Generate Clean data
# X, y = generate_data(cluster_per_c=1, class_sep=2, noise=0.1, weight_c1=0.5)
# f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
# sns.scatterplot(X[:, 0], X[:, 1], hue=y, ax=ax1)
# ax1.set_title("No Noise")
#
# # Generate noisy Data
# X, y = generate_data(cluster_per_c=1, class_sep=2, noise=0.1, weight_c1=0.5)
# sns.scatterplot(X[:, 0], X[:, 1], hue=y, ax=ax2)
# ax2.set_title("With Noise")
# plt.show()

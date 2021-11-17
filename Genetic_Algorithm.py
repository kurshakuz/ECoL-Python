import numpy as np
import pandas as pd
import rpy2.robjects as robjects
from matplotlib import pyplot as plt
from Data_Generator import generate_data
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
import seaborn as sns
from geneticalgorithm import geneticalgorithm as ga

r = robjects.r
r['source']('ECoL_complexity_functions.r')

def visualize_generated_data(min_complex, max_complex):
    X, y = generate_data(200, int(min_complex[0]), int(min_complex[1]), min_complex[2], min_complex[3])
    f, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
    sns.scatterplot(X[:, 0], X[:, 1], hue=y, ax=ax1)
    ax1.set_title("min_complex")
    X, y = generate_data(200, int(max_complex[0]), int(max_complex[1]), max_complex[2], max_complex[3])
    sns.scatterplot(X[:, 0], X[:, 1], hue=y, ax=ax2)
    ax2.set_title("max_complex")
    plt.show()



def generate_max_complexity_N1(X):
    X, y = generate_data(200, int(X[0]), int(X[1]), X[2], X[3])
    data = np.c_[ X, y]
    pd_df = pd.DataFrame(data)
    pd_df_indexed = pd_df.iloc[list(range(1, len(pd_df.index))), :]

    with localconverter(robjects.default_converter + pandas2ri.converter):
        r_from_pd_df = robjects.conversion.py2rpy(pd_df_indexed)

    neighborhood_complexity_check_function_r = robjects.globalenv['neighborhood_complexity_check']
    result_r = neighborhood_complexity_check_function_r(r_from_pd_df, 'N1')
    #convert to float
    complex_value = -result_r.rx()[0][0]
    return complex_value

def generate_min_complexity_N1(X):
    X, y = generate_data(200, int(X[0]), int(X[1]), X[2], X[3])
    data = np.c_[ X, y]
    pd_df = pd.DataFrame(data)
    pd_df_indexed = pd_df.iloc[list(range(1, len(pd_df.index))), :]

    with localconverter(robjects.default_converter + pandas2ri.converter):
        r_from_pd_df = robjects.conversion.py2rpy(pd_df_indexed)

    neighborhood_complexity_check_function_r = robjects.globalenv['neighborhood_complexity_check']
    result_r = neighborhood_complexity_check_function_r(r_from_pd_df, 'N1')
    #convert to float
    complex_value = result_r.rx()[0][0]
    return complex_value

# parameters to vary n_clusters_per_class int(1 or 2), class_seperation int(0-10), weights [(0-1),(0-1)], flip_y (0-1)
# to find parameters to generate dataset with max complex instead of min, the complex_value is negated

# varbound=np.array([[1,2],[0,2],[0.1,1],[0.1,1]])
# vartype=np.array([['int'],['int'],['real'],['real']])
# model=ga(function=generate_max_complexity_N1,dimension=4,variable_type_mixed=vartype,variable_boundaries=varbound)
#
# model.run()

#note the parameters and value will change abit each round, this is not a convex min, many combination can give min
#min found
#print(target_function([1,2,0.10167544,0.2712317]))
#should be  N1 = 0.11055276381909548
#max
#print(complexity([1,0,0.86285349,0.3744148]))
#should be  N1 = 0.8090452261306532


visualize_generated_data(min_complex=[1,2,0.10167544,0.2712317], max_complex=[1,0,0.86285349,0.3744148])
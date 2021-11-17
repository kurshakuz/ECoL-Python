import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter

r = robjects.r
r['source']('ECoL_complexity_functions.r')

# load iris dataset
pd_df = pd.read_csv('./data/iris.csv')

# data selection is done here
# supply a list of rows that will be used
# for computing the complexities
pd_df_indexed = pd_df.iloc[list(range(1, 150)), :]
print(pd_df_indexed)

with localconverter(robjects.default_converter + pandas2ri.converter):
    r_from_pd_df = robjects.conversion.py2rpy(pd_df_indexed)

# # compute complexities for whole dataset
# all_complexities_check_function_r = robjects.globalenv['all_complexities_check']
# result_r = all_complexities_check_function_r()
# print(result_r)
#
# # compute complexities for dataset subset
# all_complexities_check_subset_function_r = robjects.globalenv['all_complexities_check_subset']
# result_r = all_complexities_check_subset_function_r(r_from_pd_df)
# print(result_r)
#
# # compute complexities for the given complexity group
# # available groups are:
# # overlapping, neighborhood, linearity, dimensionality, balance, network
# group_complexity_check_function_r = robjects.globalenv['group_complexity_check']
# result_r = group_complexity_check_function_r(r_from_pd_df, 'overlapping')
# print(result_r)

# # compute feature based complexity for the given measure
# # available measures are:
# # F1, F1v, F2, F3, F4
# overlapping_complexity_check_function_r = robjects.globalenv['overlapping_complexity_check']
# result_r = overlapping_complexity_check_function_r(r_from_pd_df, 'F1')
# print(result_r)

# compute neighborhood based complexity for the given measure
# available measures are:
# N1, N2, N3, N4, T1, LSC
neighborhood_complexity_check_function_r = robjects.globalenv['neighborhood_complexity_check']
result_r = neighborhood_complexity_check_function_r(r_from_pd_df, 'N1')
print(result_r)
#
# # compute linearity based complexity for the given measure
# # available measures are:
# # L1, L2, L3
# linearity_complexity_check_function_r = robjects.globalenv['linearity_complexity_check']
# result_r = linearity_complexity_check_function_r(r_from_pd_df, 'L1')
# print(result_r)
#
# # compute dimensionality based complexity for the given measure
# # available measures are:
# # T2, T3, T4
# dimensionality_complexity_check_function_r = robjects.globalenv['dimensionality_complexity_check']
# result_r = dimensionality_complexity_check_function_r(r_from_pd_df, 'T2')
# print(result_r)
#
# # compute balance based complexity for the given measure
# # available measures are:
# # C1, C2
# balance_complexity_check_function_r = robjects.globalenv['balance_complexity_check']
# result_r = balance_complexity_check_function_r(r_from_pd_df, 'C1')
# print(result_r)
#
# # compute network based complexity for the given measure
# # available measures are:
# # Density, ClsCoef”, Hubs
# network_complexity_check_function_r = robjects.globalenv['network_complexity_check']
# result_r = network_complexity_check_function_r(r_from_pd_df, 'Density')
# print(result_r)

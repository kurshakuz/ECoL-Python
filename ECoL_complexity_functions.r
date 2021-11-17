library("ECoL")

all_complexities_check <- function(x_start_col, x_end_col, y_col) {
    return(complexity(iris[,x_start_col:x_end_col], iris[,y_col]))
}

all_complexities_check_subset <- function(input_dataframe, x_start_col, x_end_col, y_col) {
    return(complexity(input_dataframe[,x_start_col:x_end_col], as.factor(input_dataframe[,y_col])))
}

group_complexity_check <- function(input_dataframe, x_start_col, x_end_col, y_col, target_group) {
    return(complexity(input_dataframe[,x_start_col:x_end_col], as.factor(input_dataframe[,y_col]), groups=target_group))
}

overlapping_complexity_check <- function(input_dataframe, x_start_col, x_end_col, y_col, measure) {
    return(overlapping(input_dataframe[,x_start_col:x_end_col], as.factor(input_dataframe[,y_col]), measures=measure))
}

neighborhood_complexity_check <- function(input_dataframe, x_start_col, x_end_col, y_col, measure) {
    return(neighborhood(input_dataframe[,x_start_col:x_end_col], as.factor(input_dataframe[,y_col]), measures=measure))
}

linearity_complexity_check <- function(input_dataframe, x_start_col, x_end_col, y_col, measure) {
    return(linearity(input_dataframe[,x_start_col:x_end_col], as.factor(input_dataframe[,y_col]), measures=measure))
}

dimensionality_complexity_check <- function(input_dataframe, x_start_col, x_end_col, y_col, measure) {
    return(dimensionality(input_dataframe[,x_start_col:x_end_col], as.factor(input_dataframe[,y_col]), measures=measure))
}

balance_complexity_check <- function(input_dataframe, x_start_col, x_end_col, y_col, measure) {
    return(balance(input_dataframe[,x_start_col:x_end_col], as.factor(input_dataframe[,y_col]), measures=measure))
}

network_complexity_check <- function(input_dataframe, x_start_col, x_end_col, y_col, measure) {
    return(network(input_dataframe[,x_start_col:x_end_col], as.factor(input_dataframe[,y_col]), measures=measure))
}

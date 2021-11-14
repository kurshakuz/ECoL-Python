library("ECoL")

all_complexities_check <- function() {
    return(complexity(iris[,1:4], iris[,5]))
}

all_complexities_check_subset <- function(input_dataframe) {
    return(complexity(input_dataframe[,1:4], as.factor(input_dataframe[,5])))
}

group_complexity_check <- function(input_dataframe, target_group) {
    return(complexity(input_dataframe[,1:4], as.factor(input_dataframe[,5]), groups=target_group))
}

overlapping_complexity_check <- function(input_dataframe, measure) {
    return(overlapping(input_dataframe[,1:4], as.factor(input_dataframe[,5]), measures=measure))
}

neighborhood_complexity_check <- function(input_dataframe, measure) {
    return(neighborhood(input_dataframe[,1:4], as.factor(input_dataframe[,5]), measures=measure))
}

linearity_complexity_check <- function(input_dataframe, measure) {
    return(linearity(input_dataframe[,1:4], as.factor(input_dataframe[,5]), measures=measure))
}

dimensionality_complexity_check <- function(input_dataframe, measure) {
    return(dimensionality(input_dataframe[,1:4], as.factor(input_dataframe[,5]), measures=measure))
}

balance_complexity_check <- function(input_dataframe, measure) {
    return(balance(input_dataframe[,1:4], as.factor(input_dataframe[,5]), measures=measure))
}

network_complexity_check <- function(input_dataframe, measure) {
    return(network(input_dataframe[,1:4], as.factor(input_dataframe[,5]), measures=measure))
}

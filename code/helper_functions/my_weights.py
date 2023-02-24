# I've only used this function with limited data and haven't tested it --Emilio Lehoucq 3/14/23

def weights_univariate(df, col_name, weight_name, format = 'proportions', rounded = False):
    """
    Function to calculate weighted proportions or percentages.
    
    Input:
        df (dataframe). Pandas dataframe.
        col_name (string). Name of the column to weight.
        weight_name (string). Name of the column with the weights.
        format (string). Desired output: 'proportions' (default) or 'percentages'.
        rounded (Boolean). Round output to two decimals (defaults to False).
    Output:
        Pandas series with weighted proportions or percentages.
    
    Dependencies:
        The function doesn't automatically load any library, but it's designed to work with Pandas.
    
    Code inspired from:
        - https://towardsdatascience.com/how-to-analyze-survey-data-with-python-84eff9cc9568
    """
    # Subset data and group by col_name:
    grouped_data = df[[col_name, weight_name]].groupby(col_name)

    # Calculate number of weighted observations per group and in total:
    counts_per_group = grouped_data.sum()[weight_name]
    total_count = sum(counts_per_group)

    # Calculate proportions or percentages:
    if format == 'proportions':
        result = counts_per_group / total_count
    else:
        result = counts_per_group * 100 / total_count
    
    # Return result rounded or not:
    if rounded == True:
        return round(result, 2)
    else:
        return result
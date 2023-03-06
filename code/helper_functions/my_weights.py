# I've only used these function with limited data and haven't tested them --Emilio Lehoucq 3/14/23

def weights_univariate(df, col_name, weight_name, percentages = False, rounded = False):
    """
    Function to calculate weighted proportions or percentages.
    
    Input:
        df (dataframe). Pandas dataframe.
        col_name (string). Name of the column to weight.
        weight_name (string). Name of the column with the weights.
        percentages (Boolean). Output percentages rather than proportions (default).
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
    if percentages: result = counts_per_group * 100 / total_count
    else: result = counts_per_group / total_count
    
    # Return result rounded or not:
    if rounded: return round(result, 2)
    else: return result

def weights_bivariate(df, col_1_name, col_2_name, weight_name, percentages = False, rounded = False, verbose = True):
    """
    Function to calculate cross tabulated weighted proportions or percentages.
    
    Input:
        df (dataframe). Pandas dataframe.
        col_1_name (string). Name of the first column.
        col_2_name (string). Name of the second column.
        weight_name (string). Name of the column with the weights.
        percentages (Boolean). Output percentages rather than proportions (default).
        rounded (Boolean). Round output to two decimals (defaults to False).
        verbose (Boolean). Print information to explore association.
    Output:
        Pandas dataframe with weighted proportions or percentages.

    Dependencies:
        The function doesn't automatically load any library, but it's designed to work with Pandas (as pd) and matplotlib (as plt).

    Code inspired from:
        - https://towardsdatascience.com/how-to-analyze-survey-data-with-python-84eff9cc9568
    """
    # Create cross tabulations:
    xtab_counts = pd.crosstab(df[col_1_name], df[col_2_name])
    xtab_normalized = pd.crosstab(df[col_1_name], df[col_2_name], normalize = 'columns')
    xtab_weighted = pd.crosstab(df[col_1_name], df[col_2_name], df[weight_name], aggfunc = sum, dropna = True, normalize = 'columns')

    # Calculate proportions or percentages:
    if percentages:
        result = xtab_weighted * 100
        xtab_normalized = xtab_normalized * 100
    else:
        result = xtab_weighted

    # Round:
    if rounded:
        result = round(result, 2)
        xtab_normalized = round(xtab_normalized, 2)

    # Display information:
    if verbose:
        print('UNWEIGHTED TABLES (COUNTS AND NORMALIZED):\n')
        print(xtab_counts, '\n')
        print(xtab_normalized, '\n')
        print('WEIGHTED TABLE (NORMALIZED):\n')
        print(result)
        print('PLOT WITH WEIGHTED COUNTS:')
        plot = result.plot.barh(figsize = (6, 3))
        plt.show()
    
    # Return result:
    return result
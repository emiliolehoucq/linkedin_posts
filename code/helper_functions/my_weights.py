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

def weights_bivariate(df, col_1_name, col_2_name, weight_name, out_format = 'counts', rounded = False, verbose = False):
    """
    Function to calculate cross tabulated weighted counts, proportions, or percentages.
    
    Input:
        df (dataframe). Pandas dataframe.
        col_1_name (string). Name of the first categorical column.
        col_2_name (string). Name of the second categorical column.
        weight_name (string). Name of the column with the weights.
        out_format (string). Format of the output: 'counts' (default), 'proportions', or 'percentages'.
        rounded (Boolean). Round output to two decimals (defaults to False).
        verbose (Boolean). Print information to explore association (defaults to false).
    Output:
        Pandas dataframe with weighted counts, proportions, or percentages.

    Dependencies:
        The function doesn't automatically load any library, but it's designed to work with Pandas (as pd) and matplotlib (as plt).

    Code inspired from:
        - https://towardsdatascience.com/how-to-analyze-survey-data-with-python-84eff9cc9568
    """
    # Unweighted cross tabulations:
    xtab_counts = pd.crosstab(df[col_1_name], df[col_2_name])
    xtab_norm = pd.crosstab(df[col_1_name], df[col_2_name], normalize = 'columns')
    # Weighted cross tabulations:
    xtab_counts_w = pd.crosstab(df[col_1_name], df[col_2_name], df[weight_name], aggfunc = sum, dropna = True)
    xtab_norm_w = pd.crosstab(df[col_1_name], df[col_2_name], df[weight_name], aggfunc = sum, dropna = True, normalize = 'columns')

    # Format output:
    if out_format == 'counts': result = xtab_counts_w
    elif out_format == 'proportions': result = xtab_norm_w
    else: xtab_norm, result = xtab_norm * 100, xtab_norm_w * 100
        
    # Round output:
    if rounded: xtab_norm, result = round(xtab_norm, 2), round(result, 2)

    # Display information:
    if verbose:
        print('UNWEIGHTED TABLES (COUNTS AND NORMALIZED):\n')
        print(xtab_counts, '\n')
        print(xtab_norm, '\n')
        print('WEIGHTED TABLE (NORMALIZED):\n')
        print(result)
        print('PLOT (USING WEIGHTS):')
        plot = result.plot.barh(figsize = (6, 3))
        plt.show()
    
    # Return result:
    return result

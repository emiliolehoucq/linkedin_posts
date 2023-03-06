# I've only used this function with limited data and haven't tested it --Emilio Lehoucq 3/6/2023

def my_plt_style(ax, title, xgrid = False, ygrid = False, grid = False):
    """
    Function to style plot.
    
    Input:
        ax (Axes). Axes of plot.
        title (string). Title of plot. 
        xgrid (Boolean). Optional parameter to add x grid to plot. Default is false.
        ygrid (Boolean). Optional parameter to add y grid to plot. Default is false.
        grid (Boolean). Optional parameter to add both x grid and y grid to plot. Default is false.
    Output:
        None.

    Dependencies:
        The function doesn't automatically load any library, but it's designed to work with matplotlib (as plt).    
    """
    # Bold title:
    plt.title(title, fontweight = 'bold')
    
    # Remove frame around plot:
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Add grid:
    if xgrid:
        ax.xaxis.grid(linestyle = '--', color = 'lightgrey')
    elif ygrid:
        ax.yaxis.grid(linestyle = '--', color = 'lightgrey')
    elif grid:
        ax.grid(linestyle = '--', color = 'lightgrey')

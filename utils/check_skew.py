# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Scipy library
#
from scipy import stats


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Visualization libraries
#
import matplotlib.pyplot as plt
import seaborn           as sns

def check_skew(df_skew, feature):    
    '''
    Function for checking for skewness
    '''
    # Calculate skewness
    skew     = stats.skew( df_skew[ feature ] )
    skewtest = stats.skewtest( df_skew[ feature ] )

    print("{}'s: Skew: {}, : {}".format(feature, skew, skewtest))

    # Distribution plot
    #
    plt.figure(  figsize = (10, 3) )
    sns.distplot(df_skew[ feature ])
    #
    plt.title('Distribution of ' + feature)
    plt.show();
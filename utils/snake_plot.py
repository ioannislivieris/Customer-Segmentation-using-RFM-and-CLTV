
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Basic libraries
# 
import pandas as pd
import numpy as np


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Visualization libraries
#
import matplotlib.pyplot as plt
import seaborn           as sns



# Feature engine library
#
import feature_engine
from   feature_engine.outliers import Winsorizer

def snake_plot(normalised_df, labels, CustomerIDs):

    normalised_df['Cluster']    = labels
    normalised_df['CustomerID'] = CustomerIDs
    

    # Melt data into long format
    df_melt = pd.melt(normalised_df.reset_index(), 
                      id_vars    = ['CustomerID', 'Cluster'],
                      value_vars = ['Recency', 'Frequency', 'Monetary'], 
                      var_name   = 'Metric', 
                      value_name = 'Value')

    plt.figure( figsize = (15, 4) )
    sns.pointplot(data = df_melt, x = 'Metric', y = 'Value', hue = 'Cluster')

    plt.xlabel('Metric', size = 14)
    plt.ylabel('Value',  size = 14)
    plt.xticks(size = 12)
    plt.xticks(size = 12)
    plt.legend(frameon = True, fontsize = 12)
    plt.show()
    
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def preprocess_datasets(train, test):
    
    train.drop('Id', inplace=True, axis=1)
    train.drop('Id', inplace=True, axis=1)
    
def get_numeric_features(df):
    
    return pd.DataFrame(df.select_dtypes(np.number))

def plot_violins(df, n_cols=2, n_rows=7, figsize=(12,8)):
    
    """
    df: DataFrame to plot
    n_cols: Number of columns of plots to display
    n_rows: Number of rows of plots to display
    figsize: figsize of the plots
    """
    cols = get_numeric_features(df).columns
    n_cols = 2
    n_rows = 7

    for i in range(n_rows):
        fg, ax = plt.subplots(nrows=1, ncols=n_cols, figsize=(12,8))

        for j in range(n_cols):
            sns.violinplot(y=cols[i*n_cols+j], data=df, ax=ax[j])
            
def get_high_correlations(df, size=15, threshold=0.5):
    data_corr = get_numeric_features(df).corr()
    cols = data_corr.columns
    corr_list = []

    #Search for the highly correlated pairs
    for i in range(0,size): #for 'size' features
        for j in range(i+1,size): #avoid repetition
            if (data_corr.iloc[i,j] >= threshold and data_corr.iloc[i,j] < 1) or (data_corr.iloc[i,j] < 0 and data_corr.iloc[i,j] <= -threshold):
                corr_list.append([data_corr.iloc[i,j],i,j]) #store correlation and columns index

    #Sort to show higher ones first            
    s_corr_list = sorted(corr_list,key=lambda x: -abs(x[0]))

    #Print correlations and column names
    for v,i,j in s_corr_list:
        print ("%s and %s = %.2f" % (cols[i],cols[j],v))

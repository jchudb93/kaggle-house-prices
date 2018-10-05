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
    
    cols = get_numeric_features(df).columns
    n_cols = 2
    n_rows = 7

    for i in range(n_rows):
        fg, ax = plt.subplots(nrows=1, ncols=n_cols, figsize=(12,8))

        for j in range(n_cols):
            sns.violinplot(y=cols[i*n_cols+j], data=df, ax=ax[j])
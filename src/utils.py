import pandas as pd
import numpy as np

def preprocess_datasets(train, test):
    
    train.drop('Id', inplace=True, axis=1)
    train.drop('Id', inplace=True, axis=1)
    
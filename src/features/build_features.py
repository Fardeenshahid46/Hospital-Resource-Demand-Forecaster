import pandas as pd

def add_lag_features(df,target_col,lags=[1,3,7,14]):
    for lag in lags:
        df[f"{target_col}_lag{lag}"]=df[target_col].shift(lag)
    return df

def add_rolling_stats(df,target_col,window=7):
    df[f"{target_col}_rollmean"]=df[target_col].rolling(window).mean()
    df[f"{target_col}_rollstd"]=df[target_col].rolling(window).std()
    return df
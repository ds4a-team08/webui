import numpy as np
import pandas as pd

def getOveralMargin(df):
    margin_df = df['Margin'].mean()
    return margin_df

def getMarginOverTime(df):
    return df.groupby(['Date']).agg(['min', 'mean', 'max'])['Margin'].reset_index()

def getTopMargins(df, size=5):
    return df.groupby(['Brand', 'Model']).agg(['max'])['Margin'].reset_index().sort_values(by='max', ascending=False).head(size)

def getMinMargins(df, size=5):
    return df.groupby(['Brand', 'Model']).agg(['min'])['Margin'].reset_index().sort_values(by='min', ascending=True).head(size)
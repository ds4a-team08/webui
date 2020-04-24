import numpy as np
import pandas as pd

def getMarginOverTime(df):
    return df.groupby(['Date']).agg(['min', 'mean', 'max'])['Margin']

def getTopMargins(df, size):
    return df.groupby(['Brand', 'Model']).agg(['max'])['Margin'].reset_index().sort_values(by='max', ascending=False).head(size)
    

def getMinMargins(df, size=5):
    return df.groupby(['Brand', 'Model']).agg(['min'])['Margin'].reset_index().sort_values(by='min', ascending=True).head(size)


def getTopConversions(df, size=5):
    return df.groupby(['Brand', 'Model']).agg(['max'])['Conversion'].reset_index().sort_values(by='max', ascending=False).head(size)

def getBottomConversions(df, size=5):
    return df.groupby(['Brand', 'Model']).agg(['min'])['Conversion'].reset_index().sort_values(by='min', ascending=True).head(size)

def getPricingData(df):
    return df.groupby(['Brand', 'Model']).agg(['mean']).reset_index().sort_values(by='Brand', ascending=True)
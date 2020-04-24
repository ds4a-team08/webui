import numpy as np
import pandas as pd

def generateCarEntries(manufacturer, model):
    date_range = pd.date_range('2019-10-01', periods=90, freq='D')
    minimum_margin = np.random.uniform(low=0.13, high=0.16, size=len(date_range))
    average_margin = np.random.uniform(low=0.165, high=0.185, size=len(date_range))
    maximum_margin = np.random.uniform(low=0.19, high=0.23, size=len(date_range))
    df = pd.DataFrame({'date': date_range,
        'min_margin': minimum_margin,
        'avg_margin': average_margin,
        'max_margin': maximum_margin
    })
    df.set_index('date', inplace=True)
    return df

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
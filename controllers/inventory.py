import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import api
import df_functions as f
import components as c

df = api.getInventoryData().copy()
df['MarginDiff'] = df['SuggestedMargin'] - df['CurrentMargin']
df = df.sort_values(by=['MarginDiff', 'Brand', 'Model'], ascending=[False, True, True])
df = df.drop(columns=['MarginDiff'])

firstRowLayout = dbc.Row([
    dbc.Col(c.inventory.byBrandLayout(df)),
    dbc.Col(c.inventory.byModelLayout(df))
])

secondRowLayout = dbc.Row([
    dbc.Col(c.inventory.adviceLayout(df))
])

layout = html.Div([
        html.H1(children='Inventory'),
        firstRowLayout,
        secondRowLayout
    ], className='container page-content-wrapper', id="content")

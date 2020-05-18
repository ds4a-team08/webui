import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import api
import df_functions as f
import components as c

df = api.getInventoryData()

firstRowLayout = dbc.Row([
    dbc.Col(c.inventory.byBrandLayout(df)),
    dbc.Col(c.inventory.byModelLayout(df))
])

layout = html.Div([
        html.H1(children='Inventory'),
        firstRowLayout
    ], className='container page-content-wrapper', id="content")

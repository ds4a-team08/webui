import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import apps.components as c
import api
import df_functions as f

df = api.getMarginData()

first = html.Div([
        html.Div([
            c.overalMargin(f.getOveralMargin(df)),
            c.targetMargin(),
            c.marginOverTimeChart(f.getMarginOverTime(df))
        ], className='col-9'),
        html.Div([
            c.topMarginTable(f.getTopMargins(df)),
            c.minMarginTable(f.getMinMargins(df))
        ], className="col")
    ], className="row")

second = html.Div([
        html.Div([
            c.getMarginGoalMet(df)
        ])
    ], className='row')

layout = html.Div([
        html.H1(children='Margin Optimization'),
        first,
        second
    ], className='container page-content-wrapper', id="content")

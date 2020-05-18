import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
import components.sidebar as sidebar

layout = html.Div(
    [
        dbc.Button(
            html.Span([], className="navbar-toggler-icon"),
            id="collapse-button",
        ),
        dbc.Collapse(
            sidebar.layout,
            id="collapse",
        ),
    ]
)

#@app.callback(
#    Output("collapse", "is_open"),
#    [Input("collapse-button", "n_clicks")],
#    [State("collapse", "is_open")],
#)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
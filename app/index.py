import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from datetime import date, timedelta

from app import app
import controllers
from views import SidebarView
import os

DEBUG=True if 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true' else False

CONTENT_STYLE = {
    "padding": "2rem 1rem",
}

sidebar = SidebarView()

app.layout = dbc.Container([
    dbc.Row([
        dcc.Location(id='url', refresh=False),
        dbc.Col(sidebar.layout(), width=2),
        dbc.Col(id="page-content", style=CONTENT_STYLE, width=10)
    ], justify="center")
], fluid=True)

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname'), Input('time-range-slider', 'value')])
def display_page(pathname, value):
    if pathname in ['/', '/margin']:
        control = controllers.MarginController()
        endDate = date(2019, 10, 10)
        startDate = endDate - timedelta(days=value)
        control.getData(startDate, endDate)
    elif pathname == '/inventory':
        control = controllers.InventoryController()
        control.getData()
    else:
        return '404'
    return control.getLayout()

@app.callback(
    Output("margin-collapse", "is_open"),
    [Input('url', 'pathname')]
)
def toggle_margin_collpase(pathname):
    print("collapse margin")
    if pathname in ['/', '/margin']:
        return True
    return False

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=DEBUG)


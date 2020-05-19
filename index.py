import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from datetime import date, timedelta

from app import app
import controllers
import components as c
import controllers


CONTENT_STYLE = {
    "padding": "2rem 1rem",
}

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    c.sidebar.layout,
    html.Div(id="page-content", style=CONTENT_STYLE)
])

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

if __name__ == '__main__':
    app.run_server(debug=True)
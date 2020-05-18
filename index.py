import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
import controllers
import components as c


CONTENT_STYLE = {
    "padding": "2rem 1rem",
}

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    c.sidebar.layout,
    html.Div(id="page-content", style=CONTENT_STYLE)
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname in ['/', '/margin']:
        return controllers.margin.layout
    elif pathname == '/inventory':
        return controllers.inventory.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
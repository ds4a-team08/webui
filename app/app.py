import dash
import dash_bootstrap_components as dbc

meta = {
    "name": "viewport", 
    "content": "width=device-width, initial-scale=1"
}
app = dash.Dash(__name__,
    external_stylesheets=[dbc.themes.UNITED],
    meta_tags=[meta]
)
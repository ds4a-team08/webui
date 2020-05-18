import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from app import app

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

layout = html.Nav([
        html.Div([
            html.H2("Volanty")
        ], className="sidebar-header"),
        dbc.Nav(
            children=[
                dbc.NavItem(dbc.NavLink("Margin", href="/")),
                dbc.NavItem(dbc.NavLink("Inventory", href="/inventory")),
                html.HR(),
                dcc.Slider(id="time-range-slider",
                    min=5,
                    step=1,
                    max=10,
                    value=7)
            ],
            vertical=True,
            pills=True
        ),
], style=SIDEBAR_STYLE)
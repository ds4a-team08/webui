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
    "background-color": "#001E61",
    "color": "#FF5100"
}

time_range_marks = {
    5: '5',
    7: '7',
    10: '10'
}

slider = dbc.Row(dbc.Col([
            html.P('How many days to analyze?'),
            dcc.Slider(id="time-range-slider",
                marks=time_range_marks,
                min=5,
                max=10,
                step=None,
                value=5
            )
        ]))

layout = html.Nav([
    html.Div([
        html.Img(src="/assets/logo-volanty.svg")
    ], className="sidebar-header"),
    dbc.Nav(
        children=[
            dbc.NavItem(dbc.NavLink(dbc.Button("Margin", block=True, color="primary"), href="/", className="menu-link")),
            dbc.NavItem(dbc.NavLink(dbc.Button("Inventory", block=True, color="primary"), href="/inventory", className="menu-link")),
            html.Hr(),
            slider
        ],
        vertical=True,
        pills=True,
        className="sidebar-content"
    ),
], className="sidebar-body", style=SIDEBAR_STYLE)

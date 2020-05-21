import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

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

margin_nav = dbc.NavItem([
        dbc.NavLink(dbc.Button("Margin", id="margin-btn", block=True, color="primary"), href="/", className="menu-link"),
        dbc.Collapse(slider, id='margin-collapse', is_open=True)
    ])

inventory_nav = dbc.NavItem([
        dbc.NavLink(dbc.Button("Inventory", id="inventory-btn", block=True, color="primary"), href="/inventory", className="menu-link")
    ])

layout = html.Nav([
    html.Div([
        html.Img(src="/assets/logo-volanty.svg")
    ], className="sidebar-header"),
    dbc.Nav(
        children=[
            margin_nav,
            inventory_nav,
            html.Hr(),
            #slider
        ],
        vertical=True,
        pills=True,
        className="sidebar-content"
    ),
], className="sidebar-body", style=SIDEBAR_STYLE)

MN_CLICKS, INV_CLICKS = 0,0
@app.callback(
    Output("margin-collapse", "is_open"),
    [Input("margin-btn", "n_clicks"), Input("inventory-btn", "n_clicks")]
)
def toggle_margin_collpase(margin_btn_clicked, inventory_btn_clicked):
    global MN_CLICKS, INV_CLICKS
    if MN_CLICKS != margin_btn_clicked:
        MN_CLICKS = margin_btn_clicked
        return True
    if INV_CLICKS != inventory_btn_clicked:
        INV_CLICKS = inventory_btn_clicked
        return False
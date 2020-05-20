import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from app import app

class SidebarComponentBuilder:
    def __init__(self):
        self.TIME_RANGE_MARKS = {
            5: '5',
            7: '7',
            10: '10'
        }

    def header(self):
        return html.Img(src="/assets/logo-volanty.svg")

    def slider(self):
        return [html.P('How many days to analyze?'),
            dcc.Slider(id="time-range-slider",
                marks=self.TIME_RANGE_MARKS,
                min=5,
                max=10,
                step=None,
                value=5
            )]
    
    def marginButton(self):
        return dbc.Button("Margin", id="margin-btn", block=True, color="primary")
    
    def inventoryButton(self):
        return dbc.Button("Inventory", id="inventory-btn", block=True, color="primary")

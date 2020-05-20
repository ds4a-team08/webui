import dash_html_components as html
import dash_bootstrap_components as dbc

from components import SidebarComponentBuilder
import df_functions as f

class SidebarView:

    def __init__(self):
        self.builder = SidebarComponentBuilder()
        self.SIDEBAR_STYLE = {
            #"position": "fixed",
            "height": "100%", 
            "top": 0,
            "left": 0,
            "bottom": 0,
            #"width": "16rem",
            "padding": "2rem 1rem",
            "background-color": "#001E61",
            "color": "#FF5100"
        }
    
    def __header(self):
        return dbc.NavItem([
                self.builder.header()
            ], className="sidebar-header")

    def __inventoryNav(self):
        return dbc.NavItem([
                dbc.NavLink(self.builder.inventoryButton(), href="/inventory", className="menu-link")
            ])

    def __marginNav(self):
        return dbc.NavItem([
                dbc.NavLink(self.builder.marginButton(), href="/margin", className="menu-link"),
                dbc.Collapse(self.builder.slider(), id='margin-collapse', is_open=True, className="p-2")
            ])

    def layout(self):
        return dbc.Nav([
                    self.__header(),
                    self.__marginNav(),
                    self.__inventoryNav(),
                    html.Hr(),
                ],
                vertical=True,
                pills=True,
                className="p-2", \
                style=self.SIDEBAR_STYLE)
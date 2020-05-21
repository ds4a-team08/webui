import components
import dash_bootstrap_components as dbc
import dash_html_components as html


class InventoryView:
    def __init__(self):
        self.builder = components.InventoryComponentBuilder()

    def __first(self, df):
        return dbc.Row([
                dbc.Col(self.builder.byBrandLayout(df)),
                dbc.Col(self.builder.byModelLayout(df))
            ])

    def __second(self, df):
        return dbc.Row([
                dbc.Col(self.builder.adviceLayout(df))
            ])

    def layout(self, df):
        return html.Div([
                html.H1(children='Inventory'),
                self.__first(df),
                self.__second(df)
            ], className='container page-content-wrapper', id="content")

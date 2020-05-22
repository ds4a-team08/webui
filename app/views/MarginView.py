import dash_html_components as html
import dash_bootstrap_components as dbc
import df_functions as f

from components import MarginComponentBuilder


class MarginView:
    def __init__(self):
        self.builder = MarginComponentBuilder()
    
    def __header(self):
        return dbc.Row(dbc.Col(html.H1(children='Margin Tracking')))

    def __first(self, df):
        return dbc.Row([
            dbc.Col([
                self.builder.overalLayout(f.getOveralMargin(df)),
                self.builder.targetLayout(),
                self.builder.overTimeLayout(f.getMarginOverTime(df))
            ], width=9),
            dbc.Col([
                self.builder.topLayout(f.getTopMargins(df)),
                self.builder.minLayout(f.getMinMargins(df))
            ])
        ])

    def __second(self, df):
        return dbc.Row([
                dbc.Col([
                    self.builder.goalLayout(df)
                ])
            ])

    def layout(self, df):
        return dbc.Container([
                self.__header(),
                self.__first(df),
                self.__second(df)
            ], id="content")
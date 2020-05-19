import dash_html_components as html
import df_functions as f

from components import MarginComponentBuilder

class MarginView:
    def __init__(self):
        self.builder = MarginComponentBuilder()
    
    def __first(self, df):
        return html.Div([html.Div([
                    self.builder.overalLayout(f.getOveralMargin(df)),
                    self.builder.targetLayout(),
                    self.builder.overTimeLayout(f.getMarginOverTime(df))
                ], className='col-9'),
                html.Div([
                    self.builder.topLayout(f.getTopMargins(df)),
                    self.builder.minLayout(f.getMinMargins(df))
                ], className="col")
            ], className="row")

    def __second(self, df):
        return html.Div([
                html.Div([
                    self.builder.goalLayout(df)
                ])
            ], className='row')

    def layout(self, df):
        first = self.__first(df)
        second = self.__second(df)
        return html.Div([
                html.H1(children='Margin Optimization'),
                first,
                second
            ], className='container page-content-wrapper', id="content")
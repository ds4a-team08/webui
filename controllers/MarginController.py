import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import controllers.components as c
import api
import df_functions as f
from components import MarginComponentBuilder
from views import MarginView

class MarginController:
    def __init__(self):
        self.view = MarginView()

    def getData(self, startDate, endDate):
        self.df = api.getMarginData(startDate, endDate)
        print(self.df)

    def getLayout(self):
        return self.view.layout(self.df)
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

class Inventory:
    def byModelLayout(self, modelData, size=10):
        return self.__draw_pie_by_index(modelData, 'Model', 10)
    
    def byBrandLayout(self, inventoryDf, size=10):
        return self.__draw_pie_by_index(inventoryDf, 'Brand', size)
        
    def __draw_pie_by_index(self, dataDf, indexName, size):
        counts_df = dataDf[indexName].value_counts().reset_index()
        counts_df = counts_df.sort_values(by=[indexName, 'index'], ascending=[False, True])
        top_df = counts_df[:size]
        others_df = counts_df[size:]
        top_df = top_df.append({'index': 'Others', indexName: others_df[indexName].astype(int).sum()}, ignore_index=True)
        fig = px.pie(names="index", values=indexName, title=indexName+" Composition", data_frame=top_df)
        return dcc.Graph(figure=fig)

INSTANCE = Inventory()
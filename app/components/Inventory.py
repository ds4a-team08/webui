import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px


class InventoryComponentBuilder:

    def adviceLayout(self, inventoryData):
        keep_columns = ['inspectionKey','marca', 'modelo', 'versao', 'preco_por', 'current_margin', 'target_price', 'suggested_margin']
        keep_models = ['HB20', 'CRUZE', 'ONIX', 'KA', 'SANDERO', 'C3', 'CITY', 'FOX', 'LOGAN', 'PALIO']
        show_df = inventoryData[keep_columns]
        show_df = show_df[show_df['preco_por'].gt(10000)]
        show_df = show_df[show_df['suggested_margin'].between(0.16, 0.5)]
        show_df = show_df[show_df['modelo'].isin(keep_models)]
        show_df = show_df.round({'current_margin': 3, 'suggested_margin': 3})
        show_df = show_df[show_df['suggested_margin'].gt(show_df['current_margin'])]
        #show_df.loc[show_df['suggested_margin']] = show_df['suggested_margin'].round(3)
        table = dbc.Table.from_dataframe(show_df, striped=True, bordered=True, hover=True)
        return table

    def byModelLayout(self, modelData, size=10):
        return self.__draw_pie_by_index(modelData, 'modelo', 10)
    
    def byBrandLayout(self, inventoryDf, size=10):
        return self.__draw_pie_by_index(inventoryDf, 'marca', size)
        
    def __draw_pie_by_index(self, dataDf, indexName, size):
        counts_df = dataDf[indexName].value_counts().reset_index()
        counts_df = counts_df.sort_values(by=[indexName, 'index'], ascending=[False, True])
        top_df = counts_df[:size]
        others_df = counts_df[size:]
        if len(others_df) > 1:
            top_df = top_df.append({'index': 'Others', indexName: others_df[indexName].astype(int).sum()}, ignore_index=True)
        fig = px.pie(names="index", values=indexName, title=indexName, data_frame=top_df)
        return dcc.Graph(figure=fig)

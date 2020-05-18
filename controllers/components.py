import plotly.express as px
import dash_core_components as dcc
import dash_table
import pandas as pd
import dash_html_components as html

def getMarginGoalMet(df):
    goal_df = df.copy()
    goal_df["goal_met"] = goal_df['Margin'].ge(0.16)
    fig = px.pie(goal_df, names="goal_met", title="Margin Goal Met (%)")
    fig.update_layout(
        autosize=False,
        width=200,
        height=200,
        margin=dict(l=5,r=5,b=5,t=5,pad=4)
    )
    return dcc.Graph(figure=fig)

def overalMargin(value):
    return html.H4('Overal Margin: '+str(round(value, 4)))

def targetMargin(value=0.16):
    return html.H4('Target Margin: '+str(round(value, 4)))

def marginOverTimeChart(df):
    aggregation_var_name = 'aggregation'
    margin_value_var_name = 'Margin (0~1)'
    margin_over_time_df = pd.melt(df, id_vars=['Date'], var_name=aggregation_var_name, value_name=margin_value_var_name, value_vars=['min', 'mean', 'max'])
    fig = px.line(margin_over_time_df, x="Date", y=margin_value_var_name, color=aggregation_var_name, title="Margin Over Time")
    return dcc.Graph(id="margin-over-time-graph", figure=fig)

def topMarginTable(df):
    columns = [{'name': i, 'id': i} for i in df.columns]
    return html.Div([
        html.H4("Highest Margins"),
        dash_table.DataTable(data=df.to_dict(orient='records'), columns=columns, id='top-margin-table')
    ])

def minMarginTable(df):
    columns = [{'name': i, 'id': i} for i in df.columns]
    data_dict = df.to_dict(orient='records')
    output = html.Div([
        html.H4("Lowest Margins"),
        dash_table.DataTable(data=data_dict, columns=columns, id='min-margin-table')
    ])
    return output

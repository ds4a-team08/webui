from views import MarginView
import requests
import pandas as pd
import os

class MarginController:
    def __init__(self):
        self.view = MarginView()
        self.backend_url = os.environ['BACKEND_URL'] if os.environ['BACKEND_URL'] else 'http://localhost:8000'
        self.df = None

    def getData(self, startDate, endDate):
        apiResult = requests.get('{}/margin?start_date={}&end_date={}'.format(os.environ['BACKEND_URL'],startDate, endDate))
        result_df = pd.DataFrame(apiResult.json())
        result_df = result_df.set_index('Date')
        self.df = result_df

    def getLayout(self):
        if self.df is None:
            return
        return self.view.layout(self.df)
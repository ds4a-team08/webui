import pandas as pd
import views
import requests
import os

class InventoryController:
    def __init__(self):
        self.view = views.InventoryView()
        self.backend_url = os.environ['BACKEND_URL'] if 'BACKEND_URL' in os.environ else 'http://localhost:80'
        self.df = None

    def getData(self):
        apiResult = requests.get("{}/inventory".format(self.backend_url))
        # apiResult = [
        #     { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.149},
        #     { 'Brand': 'FORD', 'Model': 'FIESTA', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.148},
        #     { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.148},
        #     { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.147},
        #     { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.146},
        #     { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.13},
        #     { 'Brand': 'CITROEN', 'Model': 'C3', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.131},
        #     { 'Brand': 'CITROEN', 'Model': 'C4', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.129},
        #     { 'Brand': 'HONDA', 'Model': 'FIT', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.131},
        #     { 'Brand': 'FORD', 'Model': 'KA', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.132},
        #     { 'Brand': 'HYUNDAI', 'Model': 'HB20S', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.141},
        #     { 'Brand': 'HYUNDAI', 'Model': 'HB20X', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.14},
        #     { 'Brand': 'CHEVROLET', 'Model': 'CRUZE', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.139},
        #     { 'Brand': 'FORD', 'Model': 'FOCUS', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.155},
        #     { 'Brand': 'BMW', 'Model': '318i', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.165},
        #     { 'Brand': 'AUDI', 'Model': 'A3', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.128} ]
        df = pd.DataFrame(apiResult.json())
        df['MarginDiff'] = df['suggested_margin'] - df['current_margin']
        df = df.sort_values(by=['MarginDiff', 'marca', 'modelo'], ascending=[False, True, True])
        df = df.drop(columns=['MarginDiff'])
        self.df = df

    def getLayout(self):
        return self.view.layout(self.df)

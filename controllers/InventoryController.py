import pandas as pd
import views

class InventoryController:
    def __init__(self):
        self.view = views.InventoryView()
        return
    
    def getData(self):
        apiResult = [
            { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.149},
            { 'Brand': 'FORD', 'Model': 'FIESTA', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.148},
            { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.148},
            { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.147},
            { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.146},
            { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.13},
            { 'Brand': 'CITROEN', 'Model': 'C3', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.131},
            { 'Brand': 'CITROEN', 'Model': 'C4', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.129},
            { 'Brand': 'HONDA', 'Model': 'FIT', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.131},
            { 'Brand': 'FORD', 'Model': 'KA', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.132},
            { 'Brand': 'HYUNDAI', 'Model': 'HB20S', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.141},
            { 'Brand': 'HYUNDAI', 'Model': 'HB20X', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.14},
            { 'Brand': 'CHEVROLET', 'Model': 'CRUZE', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.139},
            { 'Brand': 'FORD', 'Model': 'FOCUS', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.155},
            { 'Brand': 'BMW', 'Model': '318i', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.165},
            { 'Brand': 'AUDI', 'Model': 'A3', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.128} ]
        df = pd.DataFrame(apiResult)
        df['MarginDiff'] = df['SuggestedMargin'] - df['CurrentMargin']
        df = df.sort_values(by=['MarginDiff', 'Brand', 'Model'], ascending=[False, True, True])
        df = df.drop(columns=['MarginDiff'])
        self.df = df
    
    def getLayout(self):
        return self.view.layout(self.df)
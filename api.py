import numpy as np
import pandas as pd

def getMarginData(start=None, end=None):
    apiResult = [
        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': 0.17, 'Date': '2019-10-01' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': 0.148, 'Date': '2019-10-01' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': 0.16, 'Date': '2019-10-01' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': 0.16, 'Date': '2019-10-01' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': 0.16, 'Date': '2019-10-01' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': 0.16, 'Date': '2019-10-01' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': 0.16, 'Date': '2019-10-01' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': 0.16, 'Date': '2019-10-01' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': 0.16, 'Date': '2019-10-01' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': 0.16, 'Date': '2019-10-01' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': 0.16, 'Date': '2019-10-01' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': 0.16, 'Date': '2019-10-01' },
        
        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': 0.169, 'Date': '2019-10-02' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': 0.15, 'Date': '2019-10-02' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': 0.16, 'Date': '2019-10-02' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': 0.16, 'Date': '2019-10-02' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': 0.16, 'Date': '2019-10-02' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': 0.16, 'Date': '2019-10-02' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': 0.16, 'Date': '2019-10-02' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': 0.16, 'Date': '2019-10-02' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': 0.16, 'Date': '2019-10-02' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': 0.16, 'Date': '2019-10-02' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': 0.16, 'Date': '2019-10-02' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': 0.16, 'Date': '2019-10-02' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': 0.168, 'Date': '2019-10-03' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': 0.152, 'Date': '2019-10-03' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': 0.16, 'Date': '2019-10-03' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': 0.16, 'Date': '2019-10-03' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': 0.16, 'Date': '2019-10-03' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': 0.16, 'Date': '2019-10-03' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': 0.16, 'Date': '2019-10-03' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': 0.16, 'Date': '2019-10-03' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': 0.16, 'Date': '2019-10-03' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': 0.16, 'Date': '2019-10-03' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': 0.16, 'Date': '2019-10-03' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': 0.16, 'Date': '2019-10-03' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': 0.167, 'Date': '2019-10-04' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': 0.153, 'Date': '2019-10-04' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': 0.16, 'Date': '2019-10-04' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': 0.16, 'Date': '2019-10-04' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': 0.16, 'Date': '2019-10-04' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': 0.16, 'Date': '2019-10-04' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': 0.16, 'Date': '2019-10-04' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': 0.16, 'Date': '2019-10-04' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': 0.16, 'Date': '2019-10-04' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': 0.16, 'Date': '2019-10-04' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': 0.16, 'Date': '2019-10-04' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': 0.16, 'Date': '2019-10-04' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': 0.166, 'Date': '2019-10-05' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': 0.151, 'Date': '2019-10-05' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': 0.16, 'Date': '2019-10-05' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': 0.16, 'Date': '2019-10-05' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': 0.16, 'Date': '2019-10-05' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': 0.16, 'Date': '2019-10-05' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': 0.16, 'Date': '2019-10-05' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': 0.16, 'Date': '2019-10-05' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': 0.16, 'Date': '2019-10-05' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': 0.16, 'Date': '2019-10-05' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': 0.16, 'Date': '2019-10-05' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': 0.16, 'Date': '2019-10-05' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': 0.165, 'Date': '2019-10-06' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': 0.148, 'Date': '2019-10-06' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': 0.16, 'Date': '2019-10-06' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': 0.16, 'Date': '2019-10-06' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': 0.16, 'Date': '2019-10-06' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': 0.16, 'Date': '2019-10-06' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': 0.16, 'Date': '2019-10-06' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': 0.16, 'Date': '2019-10-06' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': 0.16, 'Date': '2019-10-06' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': 0.16, 'Date': '2019-10-06' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': 0.16, 'Date': '2019-10-06' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': 0.16, 'Date': '2019-10-06' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': 0.167, 'Date': '2019-10-07' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': 0.153, 'Date': '2019-10-07' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': 0.16, 'Date': '2019-10-07' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': 0.16, 'Date': '2019-10-07' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': 0.16, 'Date': '2019-10-07' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': 0.16, 'Date': '2019-10-07' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': 0.16, 'Date': '2019-10-07' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': 0.16, 'Date': '2019-10-07' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': 0.16, 'Date': '2019-10-07' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': 0.16, 'Date': '2019-10-07' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': 0.16, 'Date': '2019-10-07' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': 0.16, 'Date': '2019-10-07' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': 0.163, 'Date': '2019-10-08' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': 0.157, 'Date': '2019-10-08' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': 0.16, 'Date': '2019-10-08' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': 0.16, 'Date': '2019-10-08' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': 0.16, 'Date': '2019-10-08' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': 0.16, 'Date': '2019-10-08' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': 0.16, 'Date': '2019-10-08' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': 0.16, 'Date': '2019-10-08' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': 0.16, 'Date': '2019-10-08' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': 0.16, 'Date': '2019-10-08' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': 0.16, 'Date': '2019-10-08' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': 0.16, 'Date': '2019-10-08' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': 0.163, 'Date': '2019-10-09' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': 0.157, 'Date': '2019-10-09' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': 0.16, 'Date': '2019-10-09' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': 0.16, 'Date': '2019-10-09' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': 0.16, 'Date': '2019-10-09' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': 0.16, 'Date': '2019-10-09' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': 0.16, 'Date': '2019-10-09' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': 0.16, 'Date': '2019-10-09' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': 0.16, 'Date': '2019-10-09' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': 0.16, 'Date': '2019-10-09' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': 0.16, 'Date': '2019-10-09' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': 0.16, 'Date': '2019-10-09' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': 0.163, 'Date': '2019-10-10' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': 0.157, 'Date': '2019-10-10' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': 0.16, 'Date': '2019-10-10' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': 0.16, 'Date': '2019-10-10' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': 0.16, 'Date': '2019-10-10' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': 0.16, 'Date': '2019-10-10' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': 0.16, 'Date': '2019-10-10' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': 0.16, 'Date': '2019-10-10' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': 0.16, 'Date': '2019-10-10' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': 0.16, 'Date': '2019-10-10' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': 0.16, 'Date': '2019-10-10' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': 0.16, 'Date': '2019-10-10' }

    ]
    return pd.DataFrame(apiResult)

def getInventoryData():
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
        { 'Brand': 'AUDI', 'Model': 'A3', 'Version': 'XPTO', 'VolantyPrice': 39990, 'CurrentMargin': 0.14, 'SuggestedPrice': 40100, 'SuggestedMargin': 0.128},

    ]
    return pd.DataFrame(apiResult)
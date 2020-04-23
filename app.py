import streamlit as st
import numpy as np
import pandas as pd
import time
import random
import datetime

st.sidebar.subheader("Time range")
beginningDate = st.sidebar.date_input("Begin", value=datetime.date.today().replace(day=1))
endDate = st.sidebar.date_input("End")

def getData(start=None, end=None):
    apiResult = [
        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': '0.17', 'Conversion': '0.88', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-01' },
        
        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': '0.17', 'Conversion': '0.88', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-02' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': '0.17', 'Conversion': '0.88', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-03' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': '0.17', 'Conversion': '0.88', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-04' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': '0.17', 'Conversion': '0.88', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-05' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': '0.17', 'Conversion': '0.88', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-06' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': '0.17', 'Conversion': '0.88', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-07' },

        { 'Brand': 'HYUNDAI', 'Model': 'HB20', 'Margin': '0.17', 'Conversion': '0.88', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'RENAULT', 'Model': 'SANDERO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'UP', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'FIAT', 'Model': 'UNO', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'FORD', 'Model': 'FIESTA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'FORD', 'Model': 'KA', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'VOLKSWAGEN', 'Model': 'FOX', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'HONDA', 'Model': 'FIT', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'HONDA', 'Model': 'CIVIC', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'CITROEN', 'Model': 'C3', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'CITROEN', 'Model': 'C4', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' },
        { 'Brand': 'NISSAN', 'Model': 'MARCH', 'Margin': '0.16', 'Conversion': '0.9', 'MarketPrice': 0.0, 'VolantyPrice': 0.0, 'ExpectedMargin': 0.0, 'PBuy': 0.0, 'PSelling': 0.0, 'Date': '2019-10-08' }

    ]
    return pd.DataFrame(apiResult)

def generateCarEntries(manufacturer, model):
    date_range = pd.date_range('2019-10-01', periods=90, freq='D')
    minimum_margin = np.random.uniform(low=0.13, high=0.16, size=len(date_range))
    average_margin = np.random.uniform(low=0.165, high=0.185, size=len(date_range))
    maximum_margin = np.random.uniform(low=0.19, high=0.23, size=len(date_range))
    df = pd.DataFrame({'date': date_range,
        'min_margin': minimum_margin,
        'avg_margin': average_margin,
        'max_margin': maximum_margin
    })
    df.set_index('date', inplace=True)
    return df

def getMarginOverTime(df):
    overtime_df = df.copy()
    overtime_df.set_index('date', inplace=True)
    #df = pd.concat([df, generateCarEntries('RENAULT', 'SANDERO')])
    return overtime_df

def getTopMargins(df):
    df = pd.DataFrame({
        'Brand': ['HYUNDAI', 'RENAULT', 'FORD'],
        'Model': ['HB20', 'SANDERO', 'FIESTA'],
        'Margin': [0.17, 0.16, 0.15]  
    })
    #df.set_index('Margin', inplace=True)
    return df

def getMinMargins():
    df = pd.DataFrame({
        'Brand': ['VOLKSWAGEN', 'FORD', 'FIAT'],
        'Model': ['UP', 'FOCUS', 'UNO'],
        'Margin': [0.119, 0.12, 0.121]  
    })
    #df.set_index('Margin', inplace=True)
    return df


def getTopConversions():
    df = pd.DataFrame({
        'Brand': ['VOLKSWAGEN', 'FORD', 'FIAT'],
        'Model': ['UP', 'FOCUS', 'UNO'],
        'Margin': [0.88, 0.16, 0.15]  
    })
    return df

def getBottomConversions():
    df = pd.DataFrame({
        'Brand': ['VOLKSWAGEN', 'FORD', 'FIAT'],
        'Model': ['UP', 'FOCUS', 'UNO'],
        'Margin': [0.88, 0.16, 0.15]  
    })
    return df

def getPricingData():
    df = pd.DataFrame({
        'Brand': []
    })


data = getData(beginningDate, endDate)

"""
Margin
"""
st.line_chart(getMarginOverTime())

"""
Top margins
"""
st.write(getTopMargins(data))

"""
Bottom margins
"""
st.write(getMinMargins())

"""
Top conversions
"""
st.write(getTopConversions())

"""
Bottom conversions
"""
st.write(getBottomConversions())

"""
PRICING
"""
st.write(getPricingData())

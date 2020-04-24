import streamlit as st
import numpy as np
import pandas as pd
import time
import random
import datetime
import df_functions as dff
import api

st.sidebar.subheader("Time range")
beginningDate = st.sidebar.date_input("Begin", value=datetime.date.today().replace(day=1))
endDate = st.sidebar.date_input("End")

topMarginSize = st.sidebar.slider("Top Margin Size", min_value=3, max_value=20, value=5)
bottomMarginSize = st.sidebar.slider("Bottom Margin Size", min_value=3, max_value=20, value=5)
topConversionSize = st.sidebar.slider("Top Conversion Size", min_value=3, max_value=20, value=5)
bottomConversionSize = st.sidebar.slider("Bottom Conversion Size", min_value=3, max_value=20, value=5)


data = api.getData(beginningDate, endDate)

"""
Margin
"""
st.line_chart(dff.getMarginOverTime(data))

"""
Top margins
"""
st.write(dff.getTopMargins(data, topMarginSize))

"""
Bottom margins
"""
st.write(dff.getMinMargins(data, bottomMarginSize))

"""
Top conversions
"""
st.write(dff.getTopConversions(data, topConversionSize))

"""
Bottom conversions
"""
st.write(dff.getBottomConversions(data, bottomConversionSize))

"""
PRICING
"""
st.write(dff.getPricingData(data))

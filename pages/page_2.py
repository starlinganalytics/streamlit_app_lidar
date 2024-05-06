import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Page 2 ❄️")

##Adding sliders to the page
values = st.slider(
    'Range One',
    0.0, 1001.0, (25.0, 750.0))
st.write('Values:', values)

values2 = st.slider(
    'Range Two',
    0.0, 1000.0, (250.0, 750.0))
st.write('Values:', values2)


## adding a map with a pandas dataframe with lat long columns
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

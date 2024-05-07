import open3d as o3d
import numpy as np
import streamlit as st
import plotly.graph_objects as go

# Create some sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 1, 4, 2]

# Create a Plotly figure
fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers', name='Data'))

# Render the Plotly figure in Streamlit
st.plotly_chart(fig)


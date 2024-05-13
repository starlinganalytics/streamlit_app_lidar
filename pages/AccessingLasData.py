import streamlit as st
import pandas as pd
import numpy as np

st.title("Accessing .LAS attributes using Laspy")

st.write("It is possible to build on our previous results in order to get a more customized use \
         out of Laspy. \
        \
         The following code allows us to see how we are able to incorporate \
         our load function into our workflow in order to extract the spatial coordinates \
         of our data into a numpy array which can then be utilized with any other open source \
         library in Python.")

st.code(r'''
# Function to load .las file using laspy and compress z-values 
def load_las_file(file_path, compression_factor):
    las_file = laspy.read(file_path)
    x = las_file.x * las_file.header.scale[0] + las_file.header.offset[0]
    y = las_file.y * las_file.header.scale[1] + las_file.header.offset[1]
    z = las_file.z * compression_factor * las_file.header.scale[2] + las_file.header.offset[2]
    points = np.vstack((x, y, z)).transpose()

    return points''')
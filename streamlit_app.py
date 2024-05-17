import plotly.graph_objs as go
import numpy as np
import streamlit as st
import laspy

# Embed the Plotly plot into a Streamlit app
def streamlit_app():
    st.title("Open-source LiDAR processing in Python")
    st.subheader("Written By: Juan Carlos Reyes")
    st.subheader("May 9, 2024.")

    

    mov_path = "lions_gate_1.mov"

    # Display the .mov file using st.video
    st.video(mov_path)

    st.header("Opening a .LAS file with Laspy")
    st.write("Geospatial analysts typically work with programming languages such as \
    Python due to their versatility, flexibility, and collection of open-source \
    libraries such as Laspy, Pandas, and Open3D in order to analyze and visualize \
    data related to physical locations on earth. These libraries provide a comprehensive \
    and versatile toolkit for statistical analyses and physical modeling which yield \
    invaluable insights into spatial patterns and relationships essential for \
    various applications like environmental monitoring, urban planning, and \
    even emergency response.")
    
    st.write("Although the .LAS file format is specially designed to work with major LiDAR \
              processing software, the laspy open-source library is necessary for reading, \
              filtering, and writing point cloud data into Python.")
    
    st.write("The Laspy library is freely available by means of pip install: ")

    st.code("!pip install laspy")
    
    st.write("After installing the Laspy library into Python, we can import it into our workflow with:")
    
    st.code("import laspy")
    
    st.write("Once imported, it is straightforward to load a .LAS file into a Laspy object in Python:")

    with st.echo():
        
        file_path = 'StanleyPark_100.las'
        las_file = laspy.read(file_path)
        
        las_file
        


    st.write("As we can see from printing the output, the .LAS file has been properly loaded \
            and a Laspy object has been returned. The object readout gives an overview regarding\
            the structure of the contents of the .LAS file")
    
    st.write("Upon printing the laspy object, it is possible to see the LAS data format (1.4),\
             the structure of the point format (7) along with any additional dimensions of data \
             included by the data collectors, the number of points in the dataset (), as well as the number of \
             variable length records present in the dataset. For more information regarding the use \
             of Laspy and the contents of a .LAS file please visit: \
              https://laspy.readthedocs.io/en/latest/intro.html")
    

    


    # Display the plot using Streamlit
    #st.plotly_chart(fig)

# Run the Streamlit app
if __name__ == "__main__":
    streamlit_app()

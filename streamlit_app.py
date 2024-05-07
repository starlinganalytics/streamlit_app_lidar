
import os
import subprocess

# Install OpenGL libraries if not already installed
def install_opengl_libraries():
    # Check if libGL.so.1 is present
    try:
        subprocess.check_output(['ldconfig', '-p', '|', 'grep', 'libGL.so.1'], shell=True)
    except subprocess.CalledProcessError:
        # Install libgl1-mesa-glx package
        os.system('sudo apt-get install -y libgl1-mesa-glx')
        # Update shared library cache
        os.system('sudo ldconfig')

# Check and set LD_LIBRARY_PATH if necessary
def set_ld_library_path():
    if 'LD_LIBRARY_PATH' not in os.environ:
        os.environ['LD_LIBRARY_PATH'] = '/path/to/libGL.so.1'

import plotly.graph_objs as go
import numpy as np
import streamlit as st
import open3d as o3d



# Step 1: Generate a 3D point cloud using Open3D
def generate_pointcloud():
    points = []  # Your point cloud data here, for example: [(x1, y1, z1), (x2, y2, z2), ...]
    # Generate some random points for demonstration
    for _ in range(1000):
        point = np.random.rand(3)  # Generating random 3D points
        points.append(point)
    return np.array(points)

# Step 2: Convert the point cloud data to a format that Plotly understands
def convert_to_plotly_format(pointcloud):
    x, y, z = pointcloud[:,0], pointcloud[:,1], pointcloud[:,2]
    return x, y, z

# Step 3: Create a Plotly 3D scatter plot
def create_plotly_plot(x, y, z):
    trace = go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=3))
    layout = go.Layout(scene=dict(xaxis=dict(title='X'), yaxis=dict(title='Y'), zaxis=dict(title='Z')))
    fig = go.Figure(data=[trace], layout=layout)
    return fig

# Step 4: Embed the Plotly plot into a Streamlit app
def streamlit_app():
    st.title('3D Point Cloud Visualization')
    st.write("Generated using Open3D and displayed using Plotly")

    # Generate the point cloud
    pointcloud = generate_pointcloud()

    # Convert the point cloud data
    x, y, z = convert_to_plotly_format(pointcloud)

    # Create the Plotly plot
    fig = create_plotly_plot(x, y, z)

    # Display the plot using Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Run the Streamlit app
if __name__ == "__main__":

        # Install OpenGL libraries
    install_opengl_libraries()

    # Set LD_LIBRARY_PATH
    set_ld_library_path()


    streamlit_app()




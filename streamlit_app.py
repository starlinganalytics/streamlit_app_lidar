import plotly.graph_objs as go
import numpy as np
import streamlit as st
import laspy

# Function to load .las file using laspy and get scaled coordinates
def load_las_file(file_path):
    las_file = laspy.read(file_path)
    x = las_file.x * las_file.header.scale[0] + las_file.header.offset[0]
    y = las_file.y * las_file.header.scale[1] + las_file.header.offset[1]
    z = las_file.z * las_file.header.scale[2] + las_file.header.offset[2]
    points = np.vstack((x, y, z)).transpose()
    return points

# Convert the point cloud data to a format that Plotly understands
def convert_to_plotly_format(pointcloud):
    x, y, z = pointcloud[:,0], pointcloud[:,1], pointcloud[:,2]
    return x, y, z

# Create a Plotly 3D scatter plot
def create_plotly_plot(x, y, z):
    trace = go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=3))
    layout = go.Layout(scene=dict(xaxis=dict(title='X'), yaxis=dict(title='Y'), zaxis=dict(title='Z')))
    fig = go.Figure(data=[trace], layout=layout)
    return fig

# Embed the Plotly plot into a Streamlit app
def streamlit_app():
    st.title('3D Point Cloud Visualization')
    st.write("Visualizing a .las file using Plotly in Streamlit")

    # Allow user to upload .las file
    uploaded_file = st.file_uploader("Upload .las file", type=["las"])

    if uploaded_file is not None:
        # Load the .las file
        pointcloud = load_las_file(uploaded_file)

        # Convert the point cloud data
        x, y, z = convert_to_plotly_format(pointcloud)

        # Create the Plotly plot
        fig = create_plotly_plot(x, y, z)

        # Set the size of the Plotly figure
        fig.update_layout(width=1000, height=800)

        # Display the plot using Streamlit
        st.plotly_chart(fig, use_container_width=True)

# Run the Streamlit app
if __name__ == "__main__":
    streamlit_app()

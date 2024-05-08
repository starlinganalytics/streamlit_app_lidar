import plotly.graph_objs as go
import numpy as np
import streamlit as st
import laspy

# Function to load .las file using laspy and compress z-values
def load_las_file(file_path, compression_factor):
    las_file = laspy.read(file_path)
    x = las_file.x * las_file.header.scale[0] + las_file.header.offset[0]
    y = las_file.y * las_file.header.scale[1] + las_file.header.offset[1]
    z = las_file.z * compression_factor * las_file.header.scale[2] + las_file.header.offset[2]
    points = np.vstack((x, y, z)).transpose()
    return points

# Convert the point cloud data to a format that Plotly understands
def convert_to_plotly_format(pointcloud):
    x, y, z = pointcloud[:,0], pointcloud[:,1], pointcloud[:,2]
    return x, y, z

# Create a Plotly 3D scatter plot with color based on z-coordinate values
def create_plotly_plot(x, y, z):
    # Normalize z-coordinates to [0, 1] range
    z_normalized = (z - np.min(z)) / (np.max(z) - np.min(z))
    
    # Define color scale
    colorscale = 'Viridis'  # Choose a colorscale (e.g., Viridis, Jet, etc.)
    
    # Create trace with color scale based on z-coordinate values
    trace = go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=1,
            color=z,  # Color based on z-coordinate
            colorscale=colorscale,  # Apply colorscale
            colorbar=dict(title='Z-coordinate'),  # Add colorbar with title
            opacity=0.8
        )
    )
    
    # Define layout
    layout = go.Layout(
        scene=dict(
            xaxis=dict(title='X'),
            yaxis=dict(title='Y'),
            zaxis=dict(title='Z')
        )
    )
    
    # Create figure
    fig = go.Figure(data=[trace], layout=layout)
    
    return fig

# Embed the Plotly plot into a Streamlit app
def streamlit_app():
    st.title('3D Point Cloud Visualization')
    st.write("Visualizing a .las file using Plotly in Streamlit")

    # Load the .las file with a compression factor of 0.5 (adjust as needed)
    file_path = "StanleyPark_100.las"  # File path of the .las file
    compression_factor = 3.5
    pointcloud = load_las_file(file_path, compression_factor)

    # Convert the point cloud data
    x, y, z = convert_to_plotly_format(pointcloud)

    # Create the Plotly plot with color based on z-coordinate values
    fig = create_plotly_plot(x, y, z)

    # Set the size of the Plotly canvas
    fig.update_layout(width=1000, height=800)

    # Display the plot using Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Run the Streamlit app
if __name__ == "__main__":
    streamlit_app()

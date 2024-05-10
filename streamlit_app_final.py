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

def return_colors(file_path): 
    las_file = laspy.read(file_path)

    colors = np.vstack(((las_file.red -np.asarray(las_file.red).min())/(np.asarray(las_file.red).max() - np.asarray(las_file.red).min()),
                         (las_file.green -np.asarray(las_file.green).min())/(np.asarray(las_file.green).max() - np.asarray(las_file.green).min()),
                           (las_file.blue -np.asarray(las_file.blue).min())/(np.asarray(las_file.blue).max() - np.asarray(las_file.blue).min()))).transpose()

    return colors

# Convert the point cloud data to a format that Plotly understands
def convert_to_plotly_format(points):
    x, y, z = points[:, 0], points[:, 1], points[:, 2]
    return x, y, z


def create_plotly_plot(x, y, z, colors=None):
    if colors is None:
        # If colors are not provided, use z-values to color the data
        colors = z

        # Create trace with color scale based on z-coordinate values
        trace = go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(size=1, color=colors, colorscale='Viridis')
        )
    else:
        # Create trace with color scale based on provided color values
        trace = go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(size=1, color=colors)
        )
    
    # Define layout with an expanded horizontal width and transparent background
    layout = go.Layout(
        scene=dict(
            xaxis=dict(title='X'),
            yaxis=dict(title='Y'),
            zaxis=dict(title='Z')
        ),
        width=800,
        height=800,  # Adjust the width as needed
        margin=dict(l=0),
        scene_bgcolor='rgba(0,0,0,0)'  # Set background color to transparent
    )
    
    # Create figure
    fig = go.Figure(data=[trace], layout=layout)

    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                      'paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        
    return fig

# Embed the Plotly plot into a Streamlit app
def streamlit_app():
    st.title('3D Point Cloud Visualization')
    st.write("Visualizing a .las file using Plotly in Streamlit")
    st.write("Stanley Park - Vancouver Sea Wall, British Columbia, Canada")

    # Load the .las file with a compression factor of 0.5 (adjust as needed)
    file_path = "StanleyPark_100.las"  # File path of the .las file
    compression_factor = 3.5
    points = load_las_file(file_path, compression_factor)
    
    # Add a checkbox to allow the user to choose between using color values from .las file or just z-values
    use_color_values = st.checkbox("Use Color Values from LAS file")
    if use_color_values:
        colors = return_colors(file_path)
    else:
        colors = None

    # Convert the point cloud data
    x, y, z = convert_to_plotly_format(points)

    # Create the Plotly plot with color based on z-coordinate values or color values from .las file
    fig = create_plotly_plot(x, y, z, colors)

    # Update layout to change canvas color
    fig.update_layout(
    plot_bgcolor='rgba(1,1,1,1)'  # Change canvas color to transparent 
    )

    # Display the plot using Streamlit
    st.plotly_chart(fig)

# Run the Streamlit app
if __name__ == "__main__":
    streamlit_app()

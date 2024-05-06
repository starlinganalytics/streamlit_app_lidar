import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import FastMarkerCluster, HeatMap, MarkerCluster

#Geospatial data manipulation
import pandas as pd
import geopandas as gpd
import numpy as np
#Used for working with geometrical figures 
from shapely.geometry import Point
#Used for geospatial visualization

import matplotlib.pyplot as plt


##read data with pandas
canadian_cities = pd.read_csv(r"canadacities.csv")
canadian_cities_df = pd.read_csv(r"canadacities.csv")
#create geometry column with shapely for use in geopandas
geometry_cities = [ Point(xy) for xy in zip(canadian_cities["lng"],canadian_cities["lat"])   ]
#create geodataframe object 
gdf = gpd.GeoDataFrame(canadian_cities,crs="EPSG:4326",geometry=geometry_cities)

#mean for canada
gdf_mean_lat = np.mean(gdf.lat)
gdf_mean_lng = np.mean(gdf.lng)

#nova scotia latitude and longitude
ns_lat = 44.6923
ns_lng = -62.6572
#### Using streamlit ####
#Set a title for the page
st.title("Clustering Canadian Cities", anchor=None)
st.markdown("# Welcome! This is my first streamlit app🎈!")
st.markdown("#### We are going to demonstrate some geospatial data analysis.")
st.write(" Let's take a quick look at the data which we are studying:")

if st.checkbox('Would you like to see the dataframe?'):
    #x = st.slider('x')  # 👈 this is a widget
    # Add a slider to the sidebar:
    #add_slider = st.sidebar.slider('Select a range of values',0.0, 100.0, 25.0)

    values = st.slider('Select a range of values to display from the dataframe',0, len(canadian_cities_df), (0, 10))
    st.write("The data you selected to display ranges from: ",values[0],"to ",values[1])
    st.dataframe(canadian_cities_df.iloc[values[0]:values[1]+1])


#folium map
my_map = folium.Map(tiles='OpenStreetMap',location=[ns_lat,ns_lng], zoom_start=5)
HeatMap(gdf[["lat","lng"]].values.tolist(), name='City Density', show=False, radius=10).add_to(my_map)
#add data from geoJson objects
#folium.GeoJson(data = gdf).add_to(my_map)


#fg = folium.FeatureGroup(name="city")
#fg.add_child(folium.features.GeoJson(gdf))
#my_map.add_child(fg)

#create clusters and add them to map

#my_map.add_child(FastMarkerCluster(gdf[["lat","lng"]].values.tolist(),name="Layer Name"))

locations = gdf[["lat","lng"]].values.tolist()
popup_attributes = gdf[["lat","lng","city","province_name","population","density"]].values.tolist()
popups = ["Latitude:{}<br>Longitude:{}<br>City:{}<br>Province:{}<br>Population:{}<br>Density:{}".format(
    lat, lng, city, province_name, population, density) for (lat, lng, city,province_name,population,density) in popup_attributes]

marker_cluster = MarkerCluster(
    locations=locations,
    popups=popups,
    name="1000 clustered icons",
    overlay=True,
    control=True,

)
marker_cluster.add_to(my_map)

# add a layer control to toggle the layers
folium.LayerControl().add_to(my_map)

#Adding a folium map into a render call using Streamlit.
st_data = st_folium(my_map,width=2000,height=500, returned_objects = [])



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

st.markdown("# Page 4 ❄️")


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

st.write("We are going to demonstrate some geospatial data analysis. Let's take a quick look at the data which we are studying:")
st.dataframe(canadian_cities_df.head(10))




# create a Folium map centered on the first point
map = folium.Map(location=[gdf['lat'].iloc[0], gdf['lng'].iloc[0]], zoom_start=10)

# add markers for each point in the GeoDataFrame
gdf.apply(lambda row: 
        folium.Marker(location=[row['lat'],row['lng']],
popup=f"City name: {row.city} \n lat,lon:({row.lat},{row.lng})",
tooltip=f"City name: {row.city} \n lat,lon:({row.lat},{row.lng})",
icon=folium.Icon(color="green"),
).add_to(map), axis=1)


# display the map
#### Using streamlit ####
#Set a title for the page
st.title("Adding markers to folium map.", anchor=None)

#Adding a folium map into a render call using Streamlit.
st_data = st_folium(map,width=2000,height=1000, returned_objects = [])

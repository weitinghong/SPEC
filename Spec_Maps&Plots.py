
import streamlit as st
import pandas as pd
import geopandas as gpd

st.title('Robotrucks Depot Site Selection')
st.caption("Spec Project Fall 2022")
st.caption("Marie Demple  Avichal Gupta  William Hong")


gdf_isochrone = gpd.read_file('spec_score.shp')#('spec_score.shp')

gdf_parcel = gpd.read_file('spec_score.shp')

land_gdf = gpd.read_file("base_land.shp")



geometry = gpd.points_from_xy(gdf_parcel.x, gdf_parcel.y, crs="EPSG:4326")

gdf_parcel['geometry_p'] = geometry
gdf_parcel.drop(columns=['geometry'], inplace=True)
gdf_parcel.rename(columns={'geometry_p':'geometry'}, inplace=True)
gdf_parcel.plot()

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable



fig, ax = plt.subplots(1, figsize=(15,15))
gdf_parcel.plot('zoning_cod', ax=ax, legend=True)
land_gdf.plot(ax=ax, alpha=0.1)
plt.title('All eligible parcels by zoning code')
st.pyplot(fig)

gdf_parcel = gdf_parcel.sort_values(by=['score'], ascending=False)
iso_df = gdf_parcel.head(100)



fig, ax = plt.subplots(1, figsize=(15,15))
iso_df.plot('zoning_cod', ax=ax, legend=True)
land_gdf.plot(ax=ax, alpha=0.1)
plt.title('100 top parcels by zoning code')
plt.show()
st.pyplot(fig)


import numpy as np
y = np.array([60, 22, 14, 3, 1])
mylabels = ["Limited Industrial Services", "Transit-Oriented Development", "Industrial Park", "Commercial Highway", "Major Industry"]
fig,ax = plt.subplots()
ax.pie(y, labels = mylabels, radius = 2, autopct='%1.1f%%')
plt.title('Zoning Code Distribution For Top 100 parcels', pad = 110)
#plt.show()
st.pyplot(fig)



gdf_isochrone = gdf_isochrone.sort_values(by=['score'], ascending=False)
top_isochrones = gdf_isochrone.head(100)
top_5_isochrones = gdf_isochrone.head(5)
iso_5_df = gdf_parcel.head(5)



fig, ax = plt.subplots(1, figsize=(15,15))
iso_5_df.plot('owner', legend=True, ax=ax)
top_5_isochrones.plot(ax=ax, alpha=0.1)
land_gdf.plot(ax=ax, alpha=0.2)
plt.title('Owner and service area for top 5 scoring parcels')
st.pyplot(fig)



base_land = land_gdf['geometry']
base_land.info()
base_land.to_file('base_land.shp')





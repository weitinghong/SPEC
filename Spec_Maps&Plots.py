#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd


# In[58]:


gdf_isochrone = gpd.read_file('spec_score.shp')#('spec_score.shp')


# In[59]:


gdf_parcel = gpd.read_file('spec_score.shp')


# In[50]:


land_gdf = gpd.read_file("base_land.shp")


# In[71]:


geometry = gpd.points_from_xy(gdf_parcel.x, gdf_parcel.y, crs="EPSG:4326")


# In[61]:


gdf_parcel['geometry_p'] = geometry


# In[62]:


gdf_parcel.drop(columns=['geometry'], inplace=True)


# In[63]:


gdf_parcel.rename(columns={'geometry_p':'geometry'}, inplace=True)


# In[ ]:


#!pip install streamlit


# In[65]:


import streamlit as st


# In[66]:


gdf_parcel.plot()


# In[56]:


import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


# In[86]:


fig, ax = plt.subplots(1, figsize=(15,15))
gdf_parcel.plot('zoning_cod', ax=ax, legend=True)
land_gdf.plot(ax=ax, alpha=0.1)
plt.title('All eligible parcels by zoning code')
plt.show()


# In[79]:


gdf_parcel = gdf_parcel.sort_values(by=['score'], ascending=False)
iso_df = gdf_parcel.head(100)


# In[87]:


fig, ax = plt.subplots(1, figsize=(15,15))
iso_df.plot('zoning_cod', ax=ax, legend=True)
land_gdf.plot(ax=ax, alpha=0.1)
plt.title('100 top parcels by zoning code')
plt.show()


# In[84]:


import numpy as np
y = np.array([60, 22, 14, 3, 1])
mylabels = ["Limited Industrial Services", "Transit-Oriented Development", "Industrial Park", "Commercial Highway", "Major Industry"]
plt.pie(y, labels = mylabels, radius = 2, autopct='%1.1f%%')
plt.title('Zoning Code Distribution For Top 100 parcels', pad = 110)
plt.show()


# In[88]:


gdf_isochrone = gdf_isochrone.sort_values(by=['score'], ascending=False)
top_isochrones = gdf_isochrone.head(100)


# In[89]:


top_5_isochrones = gdf_isochrone.head(5)


# In[92]:


iso_5_df = gdf_parcel.head(5)


# In[95]:


fig, ax = plt.subplots(1, figsize=(15,15))
iso_5_df.plot('owner', legend=True, ax=ax)
top_5_isochrones.plot(ax=ax, alpha=0.1)
land_gdf.plot(ax=ax, alpha=0.2)
plt.title('Owner and service area for top 5 scoring parcels')
plt.show()


# In[74]:


base_land = land_gdf['geometry']


# In[75]:


base_land.info()


# In[76]:


base_land.to_file('base_land.shp')


# In[ ]:





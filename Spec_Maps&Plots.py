#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd


# In[58]:


gdf_isochrone = gpd.read_file('spec_score.shp')
#('spec_score.shp')


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


# In[57]:


fig, ax = plt.subplots(1, figsize=(15,15))
gdf_parcel.plot('zoning_cod', ax=ax, legend=True)
land_gdf.plot(ax=ax, alpha=0.1)
plt.show()






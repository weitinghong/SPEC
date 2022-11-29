#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd


# In[5]:


# In[7]:


gpd.options.use_pygeos=True


# In[20]:


gdf_isochrone = gpd.read_file('spec_score.shp')
gdf_isochrone


# In[19]:


# In[21]:


gdf_parcel = gpd.read_file('spec_score.shp')
gdf_parcel


# In[23]:


geometry = gpd.points_from_xy(gdf_parcel.x, gdf_parcel.y, crs="EPSG:4326")
geometry


# In[25]:


gdf_parcel['geometry_p'] = geometry


# In[26]:


gdf_parcel.info()


# In[34]:


gdf_parcel.drop(columns=['geometry'], inplace=True)


# In[42]:


gdf_parcel.rename(columns={'geometry_p':'geometry'}, inplace=True)


# In[46]:


# In[47]:



# In[44]:


gdf_parcel.plot()


# In[43]:


gdf_parcel.info()


# In[ ]:


#f, ax = plt.subplots(1, figsize=(15,15))
#gdf_parcel.plot('basezone', ax=ax, legend=True)
#land_gdf.plot(ax=ax, alpha=0.1)
#plt.show()


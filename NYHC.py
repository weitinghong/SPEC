#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pacakges
import numpy as np
import pandas as pd
import os
import streamlit as st
from matplotlib import pyplot as plt

import osmnx as ox
import folium

G = ox.graph_from_place('Travis, Texas, USA', network_type='drive')
fig, ax = ox.plot_graph(ox.project_graph(G))



#plotting the figure

st.pyplot(fig)


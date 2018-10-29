# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:34:37 2018

@author: assaf
"""

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import compactness_measures as cm

### change the line below to be your favourite districting plan shapefile
districts = gpd.read_file("./cd2013/tl_rd13_us_cd113.shp")

### Compute Scores in UTM
districts = districts.to_crs({"init": "epsg:" + "32614"})
districts["UTM_PP"] = cm.polsby_popper(districts)
districts["UTM_PP_rank"] = districts["UTM_PP"].rank(ascending=False)
districts["UTM_CH"] = cm.c_hull_ratio(districts)
districts["UTM_CH_rank"] = districts["UTM_CH"].rank(ascending=False)
districts["UTM_REOCK"] = cm.reock(districts)
districts["UTM_REOCK_rank"] = districts["UTM_REOCK"].rank(ascending=False)

### Compute Scores in LATLONG
districts = districts.to_crs({"init": "epsg:" + "4326"})
districts["LATLONG_PP"] = cm.polsby_popper(districts)
districts["LATLONG_PP_rank"] = districts["LATLONG_PP"].rank(ascending=False)
districts["LATLONG_CH"] = cm.c_hull_ratio(districts)
districts["LATLONG_CH_rank"] = districts["LATLONG_CH"].rank(ascending=False)
districts["LATLONG_REOCK"] = cm.reock(districts)
districts["LATLONG_REOCK_rank"] = districts["LATLONG_REOCK"].rank(ascending=False)

### Compute Scores in CONIC
districts = districts.to_crs({"init": "esri:" + "102009"})
districts["CONIC_PP"] = cm.polsby_popper(districts)
districts["CONIC_PP_rank"] = districts["CONIC_PP"].rank(ascending=False)
districts["CONIC_CH"] = cm.c_hull_ratio(districts)
districts["CONIC_CH_rank"] = districts["CONIC_CH"].rank(ascending=False)
districts["CONIC_REOCK"] = cm.reock(districts)
districts["CONIC_REOCK_rank"] = districts["CONIC_REOCK"].rank(ascending=False)

f, ax = plt.subplots()
ax.plot(districts["CONIC_REOCK_rank"], districts["UTM_REOCK_rank"], 'o', picker=10, color='purple')
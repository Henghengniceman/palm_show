#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 15:20:35 2024

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import scienceplots
import pandas as pd 
from datetime import datetime, timedelta
import matplotlib.dates as mdates

# filename = '../Tokyo_nesting/OUTPUT/Tokyo_nesting_3d.000.nc'
ds_3d = xr.open_dataset('../OUTPUT/warm_air_bubble_with_bcm_3d.000.nc')
dt_3d = []
for dt in ds_3d['theta']['time'].values:
    dt_3d.append(pd.to_datetime('2021-01-01 09:00:00')+dt)    
ds_3d = ds_3d.assign_coords(time=dt_3d)

U  = ds_3d['u'][:,0:42,20,20]
z = U.zu_3d.values
time = U.time.values
X = np.arange(0, 54)
Y = np.arange(0, 42)
Y = U.zu_3d.values
X = U.time.values
with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(5, 1,dpi=100, figsize=(16, 9),sharex = True)
    plt.subplots_adjust(wspace=0.2,right=0.8, top=0.95,left=0.05)
    # axes.imshow(U.values.T,extent=[X.min(), X.max(), Y.min(), Y.max()], origin='lower', cmap='viridis')
    cs = ds_3d['u'][:,0:75,20,20].T.plot.imshow(
        ax=axes[0],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    cs = ds_3d['v'][:,0:75,20,20].T.plot.imshow(
        ax=axes[1],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    cs = ds_3d['w'][:,0:75,20,20].T.plot.imshow(
        ax=axes[2],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    cs = ds_3d['theta'][:,0:75,20,20].T.plot.imshow(
        ax=axes[3],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    cs = ds_3d['ql'][:,0:75,20,20].T.plot.imshow(
        ax=axes[4],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    for i in range(5):
        axes[i].xaxis.set_major_formatter(mdates.DateFormatter('%H'))
        
        
        
        
        
        
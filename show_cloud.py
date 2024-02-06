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
No = 3
ds_3d = xr.open_dataset('../Tokyo_era5_small/OUTPUT_old/Tokyo_era5_small_av_3d_N02.00'+str(No)+'.nc')
dt_3d = []
for dt in ds_3d['theta']['time'].values:
    dt_3d.append(pd.to_datetime('2020-05-01 09:00:00')+dt)    
ds_3d = ds_3d.assign_coords(time=dt_3d)

# U  = ds_3d['u'][:,0:42,20,20]
# z = U.zu_3d.values
# time = U.time.values
# X = np.arange(0, 54)
# Y = np.arange(0, 42)
# Y = U.zu_3d.values
# X = U.time.values
with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(7, 1,dpi=100, figsize=(16, 9),sharex = True)
    plt.subplots_adjust(wspace=0.2,right=0.8, top=0.95,left=0.05)
    # axes.imshow(U.values.T,extent=[X.min(), X.max(), Y.min(), Y.max()], origin='lower', cmap='viridis')
    cs = ds_3d['u'][:,0:75,12,12].T.plot.imshow(
        ax=axes[0],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    cs = ds_3d['v'][:,0:75,12,12].T.plot.imshow(
        ax=axes[1],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    cs = ds_3d['w'][:,0:75,12,12].T.plot.imshow(
        ax=axes[2],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    cs = ds_3d['theta'][:,0:75,12,12].T.plot.imshow(
        ax=axes[3],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    cs = ds_3d['ql'][:,0:75,12,12].T.plot.imshow(
        ax=axes[4],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    cs = ds_3d['qr'][:,0:75,12,12].T.plot.imshow(
        ax=axes[5],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    cs = ds_3d['q'][:,0:75,12,12].T.plot.imshow(
        ax=axes[6],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
        # vmin = 0,
        # vmax = 5,
        # levels = 11
              )
    for i in range(7):
        axes[i].xaxis.set_major_formatter(mdates.DateFormatter('%H'))

plt.savefig('../Tokyo_era5_small/figure/Tokyo_era5_small_av_3d_N02.00'+str(No)+'.png')
        
        
        
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:35:05 2023

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import scienceplots
import pandas as pd

No=4
ds_3d_av_N01 = xr.open_dataset('../Tokyo_era5_small/OUTPUT/Tokyo_era5_small_av_3d.00'+str(No)+'.nc')
dt_3d_av = []
for dt in ds_3d_av_N01['theta']['time'].values:
    dt_3d_av.append(pd.to_datetime('2020-05-01 21:00:00')+dt)    
ds_3d_av_N01 = ds_3d_av_N01.assign_coords(time=dt_3d_av)

ds_3d_av_N02 = xr.open_dataset('../Tokyo_era5_small/OUTPUT/Tokyo_era5_small_av_3d_N02.00'+str(No)+'.nc')
dt_3d_av = []
for dt in ds_3d_av_N02['theta']['time'].values:
    dt_3d_av.append(pd.to_datetime('2020-05-01 21:00:00')+dt)    
ds_3d_av_N02 = ds_3d_av_N02.assign_coords(time=dt_3d_av)

fontdicts = {'weight': 'bold', 'size': 10}
with plt.style.context(['science', 'no-latex']):
    fig, axes = plt.subplots(2, 2,dpi=100, figsize=(11, 9))
    plt.subplots_adjust(wspace=0.3, hspace=0.2,right=0.92,top=0.95,left=0.1)
    cs = ds_3d_av_N01['w'][-10,20,:,:].plot.imshow(
        ax=axes[0,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,)
    cs = ds_3d_av_N02['w'][-10,20,:,:].plot.imshow(
        ax=axes[0,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
             )
    
#     aa = ('Plot of ' + ds['theta'].attrs.get('long_name', None) 
#           + ' '*3 
#           +'t='+axes[0, 0].get_title()[14:16]+'h   '
#           +'z=50m'
#           +' '*6
#           +ds['theta'].attrs.get('units', None))
#     axes[0,0].set_title(aa)
#     # axes[0,0].set_ylim(0,2000)
#     # axes[0,0].set_yticks(np.arange(300,2000,300))
#     # axes[0,0].set_xlim(0,2000)
#     # axes[0,0].set_xticks(np.arange(300,2000,300))
    
#     cs = ds['w'][1,3,:,:].plot.contourf(
#         ax=axes[0,1],
#         robust=True,
#         cmap = 'jet',
#         add_colorbar=True,
#              )
    
#     aa = ('Plot of ' + ds['w'].attrs.get('long_name', None) 
#           + ' '*3 
#           +'t='+axes[0, 1].get_title()[14:16]+'h   '
#           +'z='+axes[0, 1].get_title()[-11:-6]+'m'
#           +' '*6
#           +ds['w'].attrs.get('units', None))
#     axes[0,1].set_title(aa)
#     axes[0,1].set_ylim(0,2000)
#     axes[0,1].set_yticks(np.arange(300,2000,300))
#     axes[0,1].set_xlim(0,2000)
#     axes[0,1].set_xticks(np.arange(300,2000,300))
    
#     cs = ds['theta'][1,10,:,:].plot.contourf(
#         ax=axes[1,0],
#         robust=True,
#         cmap = 'jet',
#         add_colorbar=True,
#              )
    
#     aa = ('Plot of ' + ds['theta'].attrs.get('long_name', None) 
#           + ' '*3 
#           +'t='+axes[1, 0].get_title()[14:16]+'h   '
#           +'z=500m'
#           +' '*6
#           +ds['theta'].attrs.get('units', None))
#     axes[1,0].set_title(aa)
#     axes[1,0].set_ylim(0,2000)
#     axes[1,0].set_yticks(np.arange(300,2000,300))
#     axes[1,0].set_xlim(0,2000)
#     axes[1,0].set_xticks(np.arange(300,2000,300))
    
#     cs = ds['w'][1,10,:,:].plot.contourf(
#         ax=axes[1,1],
#         robust=True,
#         cmap = 'jet',
#         add_colorbar=True,
#              )
    
#     aa = ('Plot of ' + ds['w'].attrs.get('long_name', None) 
#           + ' '*3 
#           +'t='+axes[1, 1].get_title()[14:16]+'h   '
#           +'z='+axes[1, 1].get_title()[-11:-6]+'m'
#           +' '*6
#           +ds['w'].attrs.get('units', None))
#     axes[1,1].set_title(aa)
#     axes[1,1].set_ylim(0,2000)
#     axes[1,1].set_yticks(np.arange(300,2000,300))
#     axes[1,1].set_xlim(0,2000)
#     axes[1,1].set_xticks(np.arange(300,2000,300))
# plt.savefig('../e1_cbl/OUTPUT/e1_cbl_5m.png')

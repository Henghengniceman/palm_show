#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:59:03 2024

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
ds_3d_av_N01 = xr.open_dataset('../OUTPUT/Tokyo_LSM_av_3d.000.nc')
dt_3d_av = []
for dt in ds_3d_av_N01['theta']['time'].values:
    dt_3d_av.append(pd.to_datetime('2021-01-01 09:00:00')+dt)    
ds_3d_av_N01 = ds_3d_av_N01.assign_coords(time=dt_3d_av)

ds_pr_N01 = xr.open_dataset('../OUTPUT/Tokyo_LSM_pr.000.nc')
dt_pr = []
for dt in ds_pr_N01['theta']['time'].values:
    dt_pr.append(pd.to_datetime('2021-01-01 09:00:00')+dt)
ds_pr_N01 = ds_pr_N01.assign_coords(time=dt_pr)

ds_ts_N01 = xr.open_dataset('../OUTPUT/Tokyo_LSM_ts.000.nc')
dt_ts = []
for dt in ds_ts_N01['E']['time'].values:
    dt_ts.append(pd.to_datetime('2021-01-01 09:00:00')+dt)
ds_ts_N01 = ds_ts_N01.assign_coords(time=dt_ts)

ds_3d_av_N02 = xr.open_dataset('../OUTPUT/Tokyo_LSM_av_3d_N02.000.nc')
dt_3d_av = []
for dt in ds_3d_av_N02['theta']['time'].values:
    dt_3d_av.append(pd.to_datetime('2021-01-01 09:00:00')+dt)    
ds_3d_av_N02 = ds_3d_av_N02.assign_coords(time=dt_3d_av)

ds_pr_N02 = xr.open_dataset('../OUTPUT/Tokyo_LSM_pr_N02.000.nc')
dt_pr = []
for dt in ds_pr_N02['theta']['time'].values:
    dt_pr.append(pd.to_datetime('2021-01-01 09:00:00')+dt)
ds_pr_N02 = ds_pr_N02.assign_coords(time=dt_pr)

fontdicts={'weight': 'bold', 'size': 10}
with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(5, 2,dpi=100, figsize=(16, 9))
    plt.subplots_adjust(wspace=0.2,right=0.9,top=0.95,left=0.05)
    cs = ds_3d_av_N01['u'][:,0:75,104,104].T.plot.imshow(
        ax=axes[0,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 0,
        vmax = 5,
        # levels = 11
              )
    
    l = 0.92
    b = 0.81
    w = 0.008
    h = 0.14
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('u (m/s)' ,labelpad =15 ) #设置colorbar的标签字体及其大小
    
    cs = ds_3d_av_N02['u'][:,0:300,256,256].T.plot.imshow(
        ax=axes[0,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 0,
        vmax = 5,
        # levels = 11
              )
    
    cs = ds_3d_av_N01['v'][:,0:75,104,104].T.plot.imshow(
        ax=axes[1,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = -2,
        vmax = 2,
        # levels = 11
              )
    
    l = 0.92
    b = 0.635
    w = 0.008
    h = 0.14
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('v (m/s)' ,labelpad =15 ) #设置colorbar的标签字体及其大小
    
    cs = ds_3d_av_N02['v'][:,0:300,256,256].T.plot.imshow(
        ax=axes[1,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = -2,
        vmax = 2,
        # levels = 11
              )
    
    U_N01  =  ds_3d_av_N01['u'][:,0:75,104,104].T
    V_N01  =  ds_3d_av_N01['v'][:,0:75,104,104].T
    
    # V_N01 = V_N01.where(V_N01 >= 0, other=0)
    wind_speed_N01 = np.sqrt(U_N01**2+V_N01**2)
    cs = wind_speed_N01.plot.imshow(
        ax=axes[2,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 0,
        vmax = 5,
        # levels = 11
              )
    
    l = 0.92
    b = 0.46
    w = 0.008
    h = 0.14
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('WS (m/s)' ,labelpad =15 ) #设置colorbar的标签字体及其大小
    
    U_N02  =  ds_3d_av_N02['u'][:,0:300,256,256].T
    V_N02  =  ds_3d_av_N02['v'][:,0:300,256,256].T
    
    # V_N02 = V_N02.where(V_N02 >= 0, other=0)
    wind_speed_N02 = np.sqrt(U_N02**2+V_N02**2)
    cs = wind_speed_N02.plot.imshow(
        ax=axes[2,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 0,
        vmax = 5,
        # levels = 11
              )
    
    cs = ds_pr_N01['w'][:,0:75].T.plot.imshow(
        ax=axes[3,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = -0.05,
        vmax = 0.05
              )
    l = 0.92
    b = 0.285
    w = 0.008
    h = 0.14
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('w (m/s)' ,labelpad =15 ) #设置colorbar的标签字体及其大小
    
    cs = ds_pr_N02['w'][:,0:300].T.plot.imshow(
        ax=axes[3,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = -0.05,
        vmax = 0.05
              )
    ds_ts_N01['rad_net'].plot(ax=axes[4,0],color ='r',lw=5)
    ds_ts_N01['rad_net'].plot(ax=axes[4,1],color ='r',lw=5)

   
    for i in range(5):
        for j in range(2):
            axes[i,j].set_title(' ')
            axes[i,j].set_xlabel(' ')
           
            axes[i,j].set_xlim(datetime(2021,1,1,10),datetime(2021,1,3,20))
            plt.setp(axes[i,j].get_xticklabels(), rotation = 0)
            custom_ticks = [datetime(2021, 1, 1, 12), 
                            datetime(2021, 1, 1, 18), 
                            datetime(2021, 1, 2, 0), 
                            datetime(2021, 1, 2, 6), 
                            datetime(2021, 1, 2, 12),
                            datetime(2021, 1, 2, 18),
                            datetime(2021, 1, 3, 0),
                            datetime(2021, 1, 3, 6),
                            datetime(2021, 1, 3, 12),
                            datetime(2021, 1, 3, 18),]
            axes[i,j].set_xticks(custom_ticks)
            axes[i,j].set_xticklabels([dt.strftime('%H') for dt in custom_ticks], ha='center')  # Center-align tick labels

    axes[4,0].set_xlabel('time')
    axes[4,1].set_xlabel('time')
    axes[0,0].set_title('D1',fontdict={'weight': 'bold', 'size': 12})
    axes[0,1].set_title('D2',fontdict={'weight': 'bold', 'size': 12})
plt.savefig('../figure/wind.png')
    
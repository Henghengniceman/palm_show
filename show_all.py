#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:31:54 2024

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import scienceplots
import pandas as pd 
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import os

No = 7
# filename = '../Tokyo_nesting/OUTPUT/Tokyo_nesting_3d.000.nc'
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

# ds_ts_N01 = xr.open_dataset('../Tokyo_era5_small/OUTPUT/Tokyo_era5_small_ts_N02.00'+str(No)+'.nc')
# dt_ts = []
# for dt in ds_ts_N01['E']['time'].values:
#     dt_ts.append(pd.to_datetime('2020-05-01 21:00:00')+dt)
# ds_ts_N01 = ds_ts_N01.assign_coords(time=dt_ts)


fontdicts={'weight': 'normal', 'size': 12}
with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(7, 2,dpi=100, figsize=(16, 9))
    plt.subplots_adjust(wspace=0.2,right=0.9,top=0.95,left=0.05)
    cs = ds_3d_av_N01['u'][:,:,4:12].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[0,0],
        robust=True,
        cmap = 'jet_r',
        add_colorbar=False,
        vmin = -10,
        vmax = 0,
        levels = 21
              )
    
    l = 0.92
    b = 0.85
    w = 0.008
    h = 0.1
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('u (m/s)' ,labelpad =15, fontdict = fontdicts) #设置colorbar的标签字体及其大小
    
    cs = ds_3d_av_N02['u'].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[0,1],
        robust=True,
        cmap = 'jet_r',
        add_colorbar=False,
        vmin = -10,
        vmax = 0,
        levels = 21
              )
    
    cs = ds_3d_av_N01['v'][:,:,4:12].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[1,0],
        robust=True,
        cmap = 'jet_r',
        add_colorbar=False,
        vmin = -3,
        vmax = -0,
        levels = 16
              )
    
    l = 0.92
    b = 0.73
    w = 0.008
    h = 0.1
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('v (m/s)' ,labelpad =15, fontdict = fontdicts) #设置colorbar的标签字体及其大小
    
    cs = ds_3d_av_N02['v'].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[1,1],
        robust=True,
        cmap = 'jet_r',
        add_colorbar=False,
        vmin = -5,
        vmax = 10,
        levels = 16
              )
    
    cs = ds_3d_av_N01['w'][:,:,4:12].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[2,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = -0.5,
        vmax = 0.5,
        levels = 21
              )
    
    l = 0.92
    b = 0.61
    w = 0.008
    h = 0.1
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('w (m/s)' ,labelpad =15, fontdict = fontdicts) #设置colorbar的标签字体及其大小
    
    cs = ds_3d_av_N02['w'].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[2,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = -0.5,
        vmax = 0.5,
        levels = 21
              )    
    cs = ds_3d_av_N01['theta'][:,:,4:12].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[3,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 288,
        vmax = 308,
        levels = 21
              )
    
    l = 0.92
    b = 0.48
    w = 0.008
    h = 0.1
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('theta (k)' ,labelpad =15, fontdict = fontdicts) #设置colorbar的标签字体及其大小
    
    cs = ds_3d_av_N02['theta'].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[3,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 288,
        vmax = 308,
        levels = 21
              )
    
   
    cs = ds_3d_av_N01['q'][:,:,4:12].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[4,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 0.004,
        vmax = 0.020,
        levels = 17
              )
    
    l = 0.92
    b = 0.35
    w = 0.008
    h = 0.1
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('q (kg/kg)' ,labelpad =15, fontdict = fontdicts) #设置colorbar的标签字体及其大小
    
    cs = ds_3d_av_N02['q'].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[4,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 0.004,
        vmax = 0.020,
        levels = 17
              )
    
    cs = ds_3d_av_N01['ql'][:,:,4:12].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[5,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 0,
        vmax = 8e-4,
        levels = 11
              )
    
    l = 0.92
    b = 0.23
    w = 0.008
    h = 0.1
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('q$_{liq}$ (kg/kg)' ,labelpad =15, fontdict = fontdicts) #设置colorbar的标签字体及其大小
    
    cs = ds_3d_av_N02['ql'].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[5,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 0.00,
        vmax = 8e-4,
        levels = 11
              )
 
    cs = ds_3d_av_N01['qr'][:,:,4:12].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[6,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 0,
        vmax = 1e-8,
        levels = 11
              )
    
    l = 0.92
    b = 0.11
    w = 0.008
    h = 0.1
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('q$_{rain}$ (kg/kg)' ,labelpad =15, fontdict = fontdicts) #设置colorbar的标签字体及其大小
    
    cs = ds_3d_av_N02['qr'].mean(axis=2).mean(axis=2).T.plot.imshow(
        ax=axes[6,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        vmin = 0.00,
        vmax = 1e-8,
        levels = 11
              )
 
    # ds_ts_N01['rad_net'].plot(ax=axes[5,0],color ='r',lw=5)
    # ds_ts_N01['rad_net'].plot(ax=axes[5,1],color ='r',lw=5)

   
    for i in range(7):
        for j in range(2):
            axes[i,j].set_title(' ')
            axes[i,j].set_xlabel(' ')
           
            axes[i,j].set_xlim(datetime(2020,5,1,22),datetime(2020,5,3,9))
            plt.setp(axes[i,j].get_xticklabels(), rotation = 0)
            custom_ticks = [datetime(2020, 5, 2, 0), 
                            datetime(2020, 5, 2, 6), 
                            datetime(2020, 5, 2, 12),
                            datetime(2020, 5, 2, 18),
                            datetime(2020, 5, 3, 0),
                            datetime(2020, 5, 3, 6),
                           
                            ]
            axes[i,j].set_xticks(custom_ticks)
            axes[i,j].set_xticklabels([dt.strftime('%H') for dt in custom_ticks], ha='center')  # Center-align tick labels
            axes[i,j].set_ylabel('z (m)')
            axes[i,j].set_ylim(0,320)
            axes[i,j].set_yticks(np.arange(0,1600,500))
    axes[4,0].set_xlabel('time')
    axes[4,1].set_xlabel('time')
    axes[0,0].set_title('D1',fontdict={'weight': 'bold', 'size': 12})
    axes[0,1].set_title('D2',fontdict={'weight': 'bold', 'size': 12})
if not os.path.exists('../Tokyo_era5_small/figure'):
            os.makedirs('../Tokyo_era5_small/figure')
            
plt.savefig('../Tokyo_era5_small/figure/cloud'+str(No)+'.png')
    
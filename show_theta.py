#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:28:45 2024

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import scienceplots
import pandas as pd 
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import matplotlib as mpl


# filename = '../Tokyo_nesting/OUTPUT/Tokyo_nesting_3d.000.nc'
ds_3d_av = xr.open_dataset('../OUTPUT/Tokyo_LSM_av_3d.000.nc')
dt_3d_av = []
for dt in ds_3d_av['theta']['time'].values:
    dt_3d_av.append(pd.to_datetime('2021-01-01 09:00:00')+dt)    
ds_3d_av = ds_3d_av.assign_coords(time=dt_3d_av)

ds_ts = xr.open_dataset('../OUTPUT/Tokyo_LSM_ts.000.nc')
dt_ts = []
for dt in ds_ts['E']['time'].values:
    dt_ts.append(pd.to_datetime('2021-01-01 09:00:00')+dt)
ds_ts = ds_ts.assign_coords(time=dt_ts)

ds_3d_av_N02 = xr.open_dataset('../OUTPUT/Tokyo_LSM_av_3d_N02.000.nc')
dt_3d_av_N02 = []
for dt in ds_3d_av_N02['theta']['time'].values:
    dt_3d_av_N02.append(pd.to_datetime('2021-01-01 09:00:00')+dt)    
ds_3d_av_N02 = ds_3d_av_N02.assign_coords(time=dt_3d_av_N02)

fontdicts={'weight': 'bold', 'size': 10}
with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(3, 1,dpi=100, figsize=(11, 9))
    plt.subplots_adjust(wspace=0,right=0.85,top=0.95,left=0.1)
    # cs = ds_3d_av['theta'][:,0:35,123:133,123:133].mean(axis=2).mean(axis=2).T.plot.contourf(
    #     ax=axes[0],
    #     robust=True,
    #     cmap = 'bwr',
    #     add_colorbar=False,
    #     # vmin = 285,
    #     # vamx = 315
    #           )
    cs = ds_3d_av['theta'][:,0:35,104,104].T.plot.imshow(
        ax=axes[0],
        robust=True,
        cmap = 'bwr',
        add_colorbar=False,
        vmin = 286,
        vmax = 313,
        levels = 10
              )
    axes[0].set_title(' ')
    coarsen_factor = 1
    # quiver = axes[0].quiver(ds_3d_av['time'][::coarsen_factor], ds_3d_av['zu_3d'][::coarsen_factor],
    #                         uda_coarse[-1, 10, :, :], vda_coarse[-1, 10, :, :], scale=50)
    # quiver = axes[0].quiver(*np.meshgrid(ds_3d_av['time'][::coarsen_factor], ds_3d_av['zu_3d'][0:35:coarsen_factor]),
    #                         ds_3d_av['u'][:,0:35,104,104].coarsen(time=coarsen_factor,zu_3d=coarsen_factor).mean(), 
    #                         ds_3d_av['v'][:,0:35,104,104].coarsen(time=coarsen_factor,zu_3d=coarsen_factor).mean(), 
    #                         scale=200,width = 0.002)
    # qk = plt.quiverkey(quiver, 0.9, -0.09, 1, r'$1$ $m/s$', labelpos='E',
    #                    coordinates='axes', fontproperties={'weight': 'bold'})

    l = 0.9
    b = 0.71
    w = 0.01
    h = 0.24
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('theta (k)' ,labelpad =15 ) #设置colorbar的标签字体及其大小
    
    cs = ds_3d_av_N02['theta'][:,0:144,256,256].T.plot.imshow(
        ax=axes[1],
        robust=True,
        cmap = 'bwr',
        add_colorbar=False,
        vmin = 286,
        vmax = 313,
        levels=10
              )
    coarsen_factor_zu = 4
    # quiver = axes[1].quiver(*np.meshgrid(ds_3d_av_N02['time'][::coarsen_factor], ds_3d_av_N02['zu_3d'][0:144:coarsen_factor_zu]),
    #                         ds_3d_av_N02['u'][:,0:144,256,256].coarsen(time=coarsen_factor,zu_3d=coarsen_factor_zu).mean(), 
    #                         ds_3d_av_N02['v'][:,0:144,256,256].coarsen(time=coarsen_factor,zu_3d=coarsen_factor_zu).mean(), 
    #                         scale=200,width = 0.002)
    # qk = plt.quiverkey(quiver, 0.9, -0.09, 1, r'$1$ $m/s$', labelpos='E',
    #                     coordinates='axes', fontproperties={'weight': 'bold'})
    axes[0].set_title(' ')
    l = 0.9
    b = 0.41
    w = 0.01
    h = 0.24
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('theta (k)' ,labelpad =15 ) #设置colorbar的标签字体及其大小


    ds_ts['rad_net'].plot(ax=axes[2],color ='r',lw=5)
    
    
    for i in range(2):
        ds_ts['zi_wtheta'].plot(ax=axes[i],color ='k',lw=2)
        axes[i].set_title(' ')
        axes[i].set_xlabel(' ')
        axes[i].set_ylabel('Altitude a.g.l. (m)')
        axes[i].set_ylim(0,1440)

    for i in range(3):
        axes[i].set_xlim(datetime(2021,1,1,10),datetime(2021,1,3,20))
        # plt.setp(axes[i].get_xticklabels(), rotation = 0)
        # axes[i].xaxis.set_major_formatter(mdates.DateFormatter('%H'))
        plt.setp(axes[i].get_xticklabels(), rotation = 0)
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
        axes[i].set_xticks(custom_ticks)
        axes[i].set_xticklabels([dt.strftime('%H') for dt in custom_ticks], ha='center')  # Center-align tick labels


    axes[0].text(datetime(2021,1,1,10,30),1450,'D1',fontdict={'weight': 'bold', 'size': 10})
    axes[1].text(datetime(2021,1,1,10,30),1450,'D2',fontdict={'weight': 'bold', 'size': 10})
    axes[2].set_xlabel('local time (UTC+9)')
plt.savefig('../figure/theta_z_t.png')    
    
    
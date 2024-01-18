#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:24:03 2024

@author: zhang
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:47:49 2024

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import scienceplots

# filename = '../Tokyo_nesting/OUTPUT/Tokyo_nesting_3d.000.nc'
ds_3d_av = xr.open_dataset('../OUTPUT/Tokyo_LSM_av_3d_N02.000.nc')
ds_3d_av = ds_3d_av.assign_coords(time=ds_3d_av['theta']['time'].values/(3600*1e9))
ds_pr = xr.open_dataset('../OUTPUT/Tokyo_LSM_pr_N02.000.nc')
ds_pr = ds_pr.assign_coords(time=ds_pr['theta']['time'].values/(3600*1e9))
ds_ts = xr.open_dataset('../OUTPUT/Tokyo_LSM_ts_N02.000.nc')
ds_ts = ds_ts.assign_coords(time=ds_ts['E']['time'].values/(3600*1e9))


fontdicts={'weight': 'bold', 'size': 10}
with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(6, 1,dpi=100, figsize=(11, 9))
    plt.subplots_adjust(wspace=0,right=0.85,top=0.95,left=0.1)
    cs = ds_3d_av['theta'][:,0:128,256,256].T.plot.contourf(
        ax=axes[0],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
        # vmin = 285,
        # vamx = 315
              )
    axes[0].set_title(' ')
    axes[0].set_xlabel(' ')
    l = 0.9
    b = 0.83
    w = 0.008
    h = 0.12
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('theta (k)' ,labelpad =15 ) #设置colorbar的标签字体及其大小
    # axes[0].set_xticklabel(' ')
    U = ds_3d_av['u'][:,:,256,256].T
    
    cs = U.plot.contourf(
        ax=axes[1],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
             )
    axes[1].set_title(' ')
    axes[1].set_xlabel(' ')
    l = 0.9
    b = 0.685
    w = 0.008
    h = 0.12
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('u (m/s)' ,labelpad =15 ) #设置colorbar的标签字体及其大小
    
    V  =  ds_3d_av['v'][:,:,256,256].T
    

    cs = V.plot.contourf(
        ax=axes[2],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
             )
    axes[2].set_title(' ')
    axes[2].set_xlabel(' ')
    l = 0.9
    b = 0.55
    w = 0.008
    h = 0.12
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('v (m/s)' ,labelpad =15 ) #设置colorbar的标签字体及其大小

    V = V.where(V >= 0, other=0)
    wind_speed = np.sqrt(U**2+V**2)
    
    cs = wind_speed.plot.contourf(
        ax=axes[3],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
             )
    axes[3].set_title(' ')
    axes[3].set_xlabel(' ')
    l = 0.9
    b = 0.40
    w = 0.008
    h = 0.12
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('ws (m/s)' ,labelpad =15 ) #设置colorbar的标签字体及其大小

    
    cs = ds_pr['v'][:,0:256].T.plot.contourf(
        ax=axes[4],
        robust=True,
        cmap = 'jet',
        add_colorbar=False,
             )
    axes[4].set_title(' ')
    axes[4].set_xlabel(' ')
    l = 0.9
    b = 0.25
    w = 0.008
    h = 0.12
    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(cs, cax=cbar_ax)
    cb.set_label('w (m/s)' ,labelpad =15 ) #设置colorbar的标签字体及其大小
    
    ds_ts['rad_net'].plot(ax=axes[5],color ='r',lw=5)
    for i in range(5):
        ds_ts['zi_wtheta'].plot(ax=axes[i],color ='w',lw=2)
    
    for i in range(6):
        axes[i].set_xlim(0,60)
    axes[5].set_xlabel('hours since simulation (hrs)')
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:05:44 2024

@author: zhang
"""
import xarray as xr
import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime 
import scienceplots 
ds_pr_N01 = xr.open_dataset('../OUTPUT/Tokyo_LSM_pr.000.nc')
dt_pr = []
for dt in ds_pr_N01['theta']['time'].values:
    dt_pr.append(pd.to_datetime('2021-01-01 09:00:00')+dt)
ds_pr_N01 = ds_pr_N01.assign_coords(time=dt_pr)

ds_pr_N02 = xr.open_dataset('../OUTPUT/Tokyo_LSM_pr_N02.000.nc')
dt_pr = []
for dt in ds_pr_N02['theta']['time'].values:
    dt_pr.append(pd.to_datetime('2021-01-01 09:00:00')+dt)
ds_pr_N02 = ds_pr_N02.assign_coords(time=dt_pr)

# var = ['u','v','w']
with plt.style.context(['science', 'no-latex']):
    fig, axes = plt.subplots(2, 3, dpi=100, figsize=(12, 9))
    plt.subplots_adjust(hspace=0.3,wspace = 0.4,right=0.92, top=0.95, left=0.1)
    for i in [0,3,4,5,6]:
        var_at_time = ds_pr_N01['u'].isel(time=i)
        var_at_time.plot(ax=axes[0,0], y='zu',label=pd.to_datetime(var_at_time.time.values).strftime('%m-%d %H:%M'))
    axes[0,0].axvline(2.5,color='grey',lw=2,ls='--')
    axes[0,0].set_ylabel('z [meters]')
    axes[0,0].set_title('u')
    axes[0,0].legend()
    axes[0,0].set_ylim(0,2000)
    
    for i in [0,3,4,5,6]:
        var_at_time = ds_pr_N01['v'].isel(time=i)
        var_at_time.plot(ax=axes[0,1], y='zv',label=pd.to_datetime(var_at_time.time.values).strftime('%m-%d %H:%M'))
    axes[0,1].axvline(0,color='grey',lw=2,ls='--')
    axes[0,1].set_ylabel('z [meters]')
    axes[0,1].set_title('v')
    # axes[0,1].legend()
    axes[0,1].set_ylim(0,2000)
    
    for i in [3,4,5,6]:
        var_at_time = ds_pr_N01['w'].isel(time=i)
        var_at_time.plot(ax=axes[0,2], y='zw',label=pd.to_datetime(var_at_time.time.values).strftime('%m-%d %H:%M'))
    # axes[0,2].axvline(0,color='grey',lw=2,ls='--')
    axes[0,2].set_ylabel('z [meters]')
    axes[0,2].set_title('w')
    # axes[0,2].legend()
    axes[0,2].set_ylim(0,2000)
    
    for i in [0,3,4,5,6]:
        var_at_time = ds_pr_N02['u'].isel(time=i)
        var_at_time.plot(ax=axes[1,0], y='zu',label=pd.to_datetime(var_at_time.time.values).strftime('%m-%d %H:%M'))
    axes[1,0].axvline(2.5,color='grey',lw=2,ls='--')
    axes[1,0].set_ylabel('z [meters]')
    axes[1,0].set_title('u')
    axes[1,0].legend()
    axes[1,0].set_ylim(0,2000)
    
    for i in [0,3,4,5,6]:
        var_at_time = ds_pr_N02['v'].isel(time=i)
        var_at_time.plot(ax=axes[1,1], y='zv',label=pd.to_datetime(var_at_time.time.values).strftime('%m-%d %H:%M'))
    axes[1,1].axvline(0,color='grey',lw=2,ls='--')
    axes[1,1].set_ylabel('z [meters]')
    axes[1,1].set_title('v')
    # axes[0,1].legend()
    axes[1,1].set_ylim(0,2000)
    
    for i in [3,4,5,6]:
        var_at_time = ds_pr_N02['w'].isel(time=i)
        var_at_time.plot(ax=axes[1,2], y='zw',label=pd.to_datetime(var_at_time.time.values).strftime('%m-%d %H:%M'))
    # axes[0,2].axvline(0,color='grey',lw=2,ls='--')
    axes[1,2].set_ylabel('z [meters]')
    axes[1,2].set_title('w')
    # axes[1,2].legend()
    axes[1,2].set_ylim(0,2000)
    
    axes[0,0].text(-2,1000,'D1',fontdict={'weight': 'bold', 'size': 15})
    axes[1,0].text(-2,1000,'D2',fontdict={'weight': 'bold', 'size': 15})

plt.savefig('../figure/wind_profile.png')
    
    
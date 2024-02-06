#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:06:52 2024

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

No = 6
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

w_N01 = ds_3d_av_N01['w'].mean(axis=2).mean(axis=2).values
w_N02 = ds_3d_av_N02['w'].mean(axis=2).mean(axis=2).values

freq_N01_cloud, edges_N01 = np.histogram(w_N01, bins=50, range=(-1, 1))
freq_N02_cloud, edges_N02 = np.histogram(w_N02, bins=50, range=(-1, 1))
w_middle_values_N01_cloud = [(edges_N01[i] + edges_N01[i+1]) / 2 for i in range(len(edges_N01)-1)]
w_middle_values_N02_cloud = [(edges_N01[i] + edges_N01[i+1]) / 2 for i in range(len(edges_N01)-1)]
w_freq_N01_cloud = freq_N01_cloud/np.sum(freq_N01_cloud)
w_freq_N02_cloud = freq_N02_cloud/np.sum(freq_N02_cloud)
#%%
ds_pr_N01 = xr.open_dataset('../Tokyo_LSM/OUTPUT/Tokyo_LSM_pr.000.nc')
dt_pr = []
for dt in ds_pr_N01['theta']['time'].values:
    dt_pr.append(pd.to_datetime('2021-01-01 09:00:00')+dt)
ds_pr_N01 = ds_pr_N01.assign_coords(time=dt_pr)

ds_pr_N02 = xr.open_dataset('../Tokyo_LSM/OUTPUT/Tokyo_LSM_pr_N02.000.nc')
dt_pr = []
for dt in ds_pr_N02['theta']['time'].values:
    dt_pr.append(pd.to_datetime('2021-01-01 09:00:00')+dt)
ds_pr_N02 = ds_pr_N02.assign_coords(time=dt_pr)

w_N01 = ds_pr_N01['w'].values
w_N02 = ds_pr_N02['w'].values

freq_N01_cloud, edges_N01 = np.histogram(w_N01, bins=50, range=(-0.015, 0.015))
freq_N02_cloud, edges_N02 = np.histogram(w_N02, bins=50, range=(-0.015, 0.015))
w_middle_values_N01_LSM = [(edges_N01[i] + edges_N01[i+1]) / 2 for i in range(len(edges_N01)-1)]
w_middle_values_N02_LSM = [(edges_N01[i] + edges_N01[i+1]) / 2 for i in range(len(edges_N01)-1)]
w_freq_N01_LSM = freq_N01_cloud/np.sum(freq_N01_cloud)
w_freq_N02_LSM = freq_N02_cloud/np.sum(freq_N02_cloud)



with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(1, 2,dpi=100, figsize=(12, 6))
   
    axes[0].plot(w_middle_values_N01_cloud,w_freq_N01_cloud,lw=2,label='N01')
    axes[0].plot(w_middle_values_N02_cloud,w_freq_N02_cloud,lw=2,label='N02')
    axes[0].legend()
    # ds_pr_N01['theta'][0,:].plot(ax=axes[0],y='ztheta',label='constant3')
    
    axes[0].set_title(' ')
    axes[0].set_xlabel('w (m/s)')
    axes[0].set_ylabel('PDF')
    
    axes[1].plot(w_middle_values_N01_LSM,w_freq_N01_LSM,lw=2,label='N01')
    axes[1].plot(w_middle_values_N02_LSM,w_freq_N02_LSM,lw=2,label='N02')
    axes[1].legend()
    # ds_pr_N01['theta'][0,:].plot(ax=axes[0],y='ztheta',label='constant3')
    
    axes[1].set_title(' ')
    axes[1].set_xlabel('w (m/s)')
    axes[1].set_ylabel('PDF')

plt.savefig('../Tokyo_era5_small/figure/pdf_w.png')
# print(np.nanmax(w_N01))
# print(np.nanmin(w_N01))
# print(np.nanmax(w_N02))
# print(np.nanmin(w_N02))

# wind_range = np.arange(-6.5,6.6,0.5)
# for i in range(w_N01.shape[0]):
#     for j in range(w_N01.shape[1]):
        
        
        










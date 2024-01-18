#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:52:39 2024

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import scienceplots
from datetime import datetime

filename = '../OUTPUT/Tokyo_LSM_pr.000.nc'
ds = xr.open_dataset(filename)
theta = ds['theta']
with plt.style.context(['science', 'no-latex']):
    fig, axes = plt.subplots(1, 3, dpi=100, figsize=(16, 6))
    plt.subplots_adjust(wspace=0.3, hspace=0.2, right=0.92, top=0.95, left=0.1)
    
    # Loop through different time steps
    for i in range(6):
        theta_at_time = ds['theta'].isel(time=i)
        # Select a specific time step (adjust the index as needed)
        time_values_datetime = theta_at_time.time.values.astype(datetime)
        hours, remainder = divmod(time_values_datetime, 3_600_000_000_000)  # 1 hour in nanoseconds
        minutes, _ = divmod(remainder, 60_000_000_000)  # 1 minute in nanoseconds
        time = str(hours).zfill(2)+':'+str(minutes).zfill(2)
        theta_at_time.plot(ax=axes[0], y='ztheta', label=time)
    axes[0].set_ylabel('z [meters]')
    axes[0].set_title('theta')
    axes[0].legend()
    
    # for i in range(len(ds['time'])):
    #     wtheta_at_time = ds['wtheta'].isel(time=i)
    #     # Select a specific time step (adjust the index as needed)
    #     time_values_datetime = wtheta_at_time.time.values.astype(datetime)
    #     hours, remainder = divmod(time_values_datetime, 3_600_000_000_000)  # 1 hour in nanoseconds
    #     minutes, _ = divmod(remainder, 60_000_000_000)  # 1 minute in nanoseconds
    #     time = str(hours).zfill(2)+':'+str(minutes).zfill(2)
    #     wtheta_at_time.plot(ax=axes[1], y='zwtheta', label=time)
    # axes[1].set_xlim(-0.03,0.15)
    # axes[1].set_xticks(np.arange(0, 0.15, 0.03))
    # axes[1].set_ylabel('z [meters]')
    # axes[1].set_title('wtheta')
    # axes[1].legend()
    
    # for i in range(-2,-1):
    #     wtheta_at_time = ds['wtheta'].isel(time=i)
    #     wtheta_sgs = ds['w"theta"'].isel(time=i)
    #     wtheta_res = ds['w*theta*'].isel(time=i)
    #     # Select a specific time step (adjust the index as needed
    #     wtheta_at_time.plot(ax=axes[2], y='zwtheta',lw=2,color='r',ls='solid',label='zwtheta')
    #     wtheta_sgs.plot(ax=axes[2], y='zw"theta"',lw=2,color='g',ls='dotted',label='zw"theta"')
    #     wtheta_res.plot(ax=axes[2], y='zw*theta*',lw=2,color='b',ls='dashed',label='zw*theta*')
    # axes[2].set_xlim(-0.03,0.15)
    # axes[2].set_xticks(np.arange(0, 0.15, 0.03))
    # axes[2].set_ylabel('z [meters]')
    # axes[2].set_title('wtheta')
    # axes[2].legend()
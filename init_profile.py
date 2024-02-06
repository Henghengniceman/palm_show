#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:55:42 2024

@author: zhang
"""
No=3
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
from metpy.calc import relative_humidity_from_mixing_ratio
from metpy.units import units

from metpy.calc import height_to_pressure_std
ds = xr.open_dataset('/Users/zhang/Documents/WRF/202005/WRF4PALM/dynamic_files/wrf4palm_small_dynamic_2020_5_1_12')
ds_pr_N01 = xr.open_dataset('../Tokyo_era5_small/OUTPUT/Tokyo_era5_small_pr.00'+str(No)+'.nc')
dt_pr = []
for dt in ds_pr_N01['q']['time'].values:
    dt_pr.append(pd.to_datetime('2020-05-01 21:00:00')+dt)
ds_pr_N01 = ds_pr_N01.assign_coords(time=dt_pr)

height_constant  = ds_pr_N01['theta'][0,:].ztheta.values
pressure_constant = height_to_pressure_std(height_constant * units.meters)
tem_constant = ds_pr_N01['theta'][0,:].values-273
q_constant =ds_pr_N01['q'][0,:].values
rh_constant = relative_humidity_from_mixing_ratio(pressure_constant,
                                    tem_constant * units.degC, q_constant).to('percent')

height_wrf = ds['init_atmosphere_pt'].z.values
pressure_wrf = height_to_pressure_std(height_wrf * units.meters)

tem_wrf = ds['init_atmosphere_pt'].values-273
q_wrf =ds['init_atmosphere_qv'].values
rh_wrf = relative_humidity_from_mixing_ratio(pressure_wrf,
                                    tem_wrf * units.degC, q_wrf).to('percent')

tem_sim = list(np.arange(293.5,293.8,0.04))+list(np.arange(294.14,299,0.34))+list(np.arange(299.09,301.49,0.09))
print(len(tem_sim))

qv_sim = list(np.arange(0.0105,0.007,-2.2e-4))+list(np.arange(0.00692,0.00568,-8e-5))+list(np.arange(0.00567,0.00547,-1.12e-5))
print(len(qv_sim))

qv_sim2 = list(np.arange(0.021,0.014,-4.4e-4))+list(np.arange(0.01384,0.01136,-1.6e-4))+list(np.arange(0.01134,0.01094,-2.24e-5))
print(len(qv_sim2))
tem_sim = np.array(tem_sim)-273
qv_sim = np.array(qv_sim)
qv_sim2 = np.array(qv_sim2)

rh_sim = relative_humidity_from_mixing_ratio(pressure_wrf,
                                    tem_sim * units.degC, qv_sim).to('percent')

rh_sim2 = relative_humidity_from_mixing_ratio(pressure_wrf,
                                    tem_sim * units.degC, qv_sim2).to('percent')


with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(1, 3,dpi=100, figsize=(15, 6))
    ds['init_atmosphere_pt'].plot(ax = axes[0],y='z',label = 'wrf')
    axes[0].plot(tem_sim+273,height_wrf,label='Constant 1,2')
    # ds_pr_N01['theta'][0,:].plot(ax=axes[0],y='ztheta',label='constant3')
    axes[0].legend()
    axes[0].set_title(' ')
    axes[0].set_xlabel('init_atmposphere_theta (K)')
    
    ds['init_atmosphere_qv'].plot(ax = axes[1],y='z',label = 'wrf')
    axes[1].plot(qv_sim,height_wrf,label='constant1')
    axes[1].plot(qv_sim2,height_wrf,label='constant2')
    # ds_pr_N01['q'][0,:].plot(ax=axes[1],y='zq',label='constant3')
    axes[1].legend()
    axes[1].set_title(' ')
    axes[1].set_xlabel('init_atmposphere_water_vapor (kg/kg)')
    axes[2].plot(rh_wrf,height_wrf,label='wrf')
    # axes[2].plot(rh_constant,height_constant)
    axes[2].plot(rh_sim,height_wrf,label = 'constant1')
    axes[2].plot(rh_sim2,height_wrf,label = 'constant2')
    axes[2].legend()
    axes[2].set_xlabel('relative_humidity (%)')
    axes[2].set_ylabel('z (m)')
plt.savefig('../Tokyo_era5_small/figure/cloud_init.png')



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:35:05 2023

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt

filename = '../e1_cbl/OUTPUT/e1_cbl_3d.000.nc'
ds = xr.open_dataset(filename)
thetada = ds['theta'][-1,3,:,:] # 3hr, 
import numpy as np

fontdicts={'weight': 'bold', 'size': 10}
with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(2, 2,dpi=100, figsize=(11, 9))
    plt.subplots_adjust(wspace=0.3, hspace=0.2,right=0.92,top=0.95,left=0.1)
    cs = ds['theta'][-1,3,:,:].plot.contourf(
        ax=axes[0,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
             )
    subplot_title = axes[0, 0].get_title()
    
    aa = ('Plot of ' + ds['theta'].attrs.get('long_name', None) 
          + ' '*3 
          +'t='+axes[0, 0].get_title()[14:16]+'h   '
          +'z='+axes[0, 0].get_title()[-11:-6]+'m'
          +' '*6
          +ds['theta'].attrs.get('units', None))
    axes[0,0].set_title(aa)
    axes[0,0].set_ylim(0,2000)
    axes[0,0].set_yticks(np.arange(300,2000,300))
    axes[0,0].set_xlim(0,2000)
    axes[0,0].set_xticks(np.arange(300,2000,300))
    print(aa)
# all_data_vars = ds.data_vars

# # 打印数据变量字典
# print(all_data_vars)

# # 遍历所有数据变量并打印信息
# for var_name, data_array in all_data_vars.items():
#     print(f"Variable: {var_name}")
#     print(data_array)
#     print("----------------------")


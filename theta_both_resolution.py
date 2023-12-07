#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:48:12 2023

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import scienceplots


ds_50 = xr.open_dataset('../e1_cbl/OUTPUT/e1_cbl_3d.001.nc')
ds_5 = xr.open_dataset('../e1_cbl/OUTPUT/e1_cbl_3d.000.nc')

fontdicts={'weight': 'bold', 'size': 10}
with plt.style.context(['science','no-latex']):
    fig, axes = plt.subplots(2, 2,dpi=100, figsize=(11, 9))
    plt.subplots_adjust(wspace=0.3, hspace=0.2,right=0.92,top=0.95,left=0.1)
    cs = ds_50['theta'][-1,3,:,:].plot.contourf(
        ax=axes[0,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
             )
    
    aa = ('Plot of ' + ds_50['theta'].attrs.get('long_name', None) 
          + ' '*3 
          +'t='+axes[0, 0].get_title()[14:16]+'h   '
          +'z='+axes[0, 0].get_title()[-11:-6]+'m'
          +' '*6
          +ds_50['theta'].attrs.get('units', None))
    axes[0,0].set_title(aa)
    axes[0,0].set_ylim(0,2000)
    axes[0,0].set_yticks(np.arange(300,2000,300))
    axes[0,0].set_xlim(0,2000)
    axes[0,0].set_xticks(np.arange(300,2000,300))
    
    cs = ds_5['theta'][-1,26,:,:].plot.contourf(
        ax=axes[0,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
             )
    
    aa = ('Plot of ' + ds_5['theta'].attrs.get('long_name', None) 
          + ' '*3 
          +'t='+axes[0, 1].get_title()[14:16]+'h   '
          +'z='+axes[0, 1].get_title()[-11:-6]+'m'
          +' '*6
          +ds_5['theta'].attrs.get('units', None))
    axes[0,1].set_title(aa)
    axes[0,1].set_ylim(0,2000)
    axes[0,1].set_yticks(np.arange(300,2000,300))
    axes[0,1].set_xlim(0,2000)
    axes[0,1].set_xticks(np.arange(300,2000,300))
    
    cs = ds_50['theta'][-1,10,:,:].plot.contourf(
        ax=axes[1,0],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
             )
    
    aa = ('Plot of ' + ds_50['theta'].attrs.get('long_name', None) 
          + ' '*3 
          +'t='+axes[1, 0].get_title()[14:16]+'h   '
          +'z='+axes[1, 0].get_title()[-11:-6]+'m'
          +' '*6
          +ds_50['theta'].attrs.get('units', None))
    axes[1,0].set_title(aa)
    axes[1,0].set_ylim(0,2000)
    axes[1,0].set_yticks(np.arange(300,2000,300))
    axes[1,0].set_xlim(0,2000)
    axes[1,0].set_xticks(np.arange(300,2000,300))
    
    cs = ds_50['w'][-1,10,:,:].plot.contourf(
        ax=axes[1,1],
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
             )
    
    aa = ('Plot of ' + ds_50['w'].attrs.get('long_name', None) 
          + ' '*3 
          +'t='+axes[1, 1].get_title()[14:16]+'h   '
          +'z='+axes[1, 1].get_title()[-11:-6]+'m'
          +' '*6
          +ds_50['w'].attrs.get('units', None))
    axes[1,1].set_title(aa)
    axes[1,1].set_ylim(0,2000)
    axes[1,1].set_yticks(np.arange(300,2000,300))
    axes[1,1].set_xlim(0,2000)
    axes[1,1].set_xticks(np.arange(300,2000,300))
plt.savefig('../figure/e1_cbl_50m.png')

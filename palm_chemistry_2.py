#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:53:24 2023

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import scienceplots

filename = '../e5_chem/chem_phstatp/OUTPUT/chem_phstatp_3d.000.nc'
ds_phastatp = xr.open_dataset(filename)
filename = '../e5_chem/chem_smog/OUTPUT/chem_smog_3d.000.nc'
ds_smog = xr.open_dataset(filename)

var = ['kc_O3']
with plt.style.context(['science','no-latex']):
    fig = plt.figure(dpi=100, figsize=(11, 4))
    plt.subplots_adjust(wspace=0.3, hspace=0.2,right=0.92,top=0.95,left=0.1)
    
    ax = fig.add_subplot(1, 2, 1)
    cs = ds_phastatp[var[0]][-1,1,:,:].plot.contourf(
        ax=ax,
        robust=True,
        vmin =0.03, 
        vmax = 0.042,
        cmap = 'jet',
        add_colorbar=True,
             )
    title = (ds_phastatp[var[0]].attrs.get('long_name', None)
            + ' '*2
            +'phstatp  '
            +'t='+ax.get_title()[14:16]+'h   '
            +'z='+ax.get_title()[-11:-7]+'m'
            +' '*2
            +ds_phastatp[var[0]].attrs.get('units', None))
    ax.set_title(title)
    
    ax = fig.add_subplot(1, 2, 2)
    cs = ds_smog[var[0]][-1,1,:,:].plot.contourf(
        ax=ax,
        vmin =0.03, 
        vmax = 0.042,
        robust=True,
        cmap = 'jet',
        add_colorbar=True,
             )
    title = (ds_smog[var[0]].attrs.get('long_name', None)
            + ' '*2
            +'smog  '
            +'t='+ax.get_title()[14:16]+'h   '
            +'z='+ax.get_title()[-11:-7]+'m'
            +' '*2
            +ds_smog[var[0]].attrs.get('units', None))
    ax.set_title(title)


plt.savefig('../e5_chem/chem_phstatp/OUTPUT/xy_gas_phstatp_smog.png')

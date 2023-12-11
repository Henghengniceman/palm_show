#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 13:34:02 2023

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import scienceplots

filename = '../e5_chem/chem_phstatp/OUTPUT/chem_phstatp_3d.000.nc'
ds = xr.open_dataset(filename)

var = ['kc_NO','kc_NO2','kc_O3','kc_PM10']
No =ds[var[0]][-1,1,:,:]
with plt.style.context(['science','no-latex']):
    fig = plt.figure(dpi=100, figsize=(11, 9))
    plt.subplots_adjust(wspace=0.3, hspace=0.2,right=0.92,top=0.95,left=0.1)
    for i in range(len(var)):
        ax = fig.add_subplot(2, 2, i+1)
        cs = ds[var[i]][-1,1,:,:].plot.contourf(
            ax=ax,
            robust=True,
            cmap = 'jet',
            add_colorbar=True,
                 )
        title = (ds[var[i]].attrs.get('long_name', None)
                + ' '*6
                +'t='+ax.get_title()[14:16]+'h   '
                +'z='+ax.get_title()[-11:-7]+'m'
                +' '*6
                +ds[var[i]].attrs.get('units', None))
        ax.set_title(title)

plt.savefig('../e5_chem/chem_phstatp/OUTPUT/xy_gas.png')


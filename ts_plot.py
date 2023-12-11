#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:26:20 2023

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import scienceplots
from datetime import datetime

filename = '../e1_cbl/OUTPUT/e1_cbl_ts.000.nc'
ds = xr.open_dataset(filename)
var = ['E*','wmax','wtheta','w*']
with plt.style.context(['science', 'no-latex']):
    fig, axes = plt.subplots(4, 1, dpi=100, figsize=(9, 9))
    plt.subplots_adjust(hspace=0.3,right=0.92, top=0.95, left=0.1)
    for i in range(len(var)):
        axes[i].plot(ds[var[i]].time/1e9,ds[var[i]].values)
        title = (ds[var[i]].attrs.get('long_name', None)
                 + ' ' * 125
                 + ds[var[i]].attrs.get('units', None))
        axes[i].set_title(title)
        axes[i].set_xlabel('t(s)')
        
plt.savefig('../e1_cbl/OUTPUT/ts.png')        
        
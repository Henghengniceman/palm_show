#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:24:59 2023

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import scienceplots

filename = '../e1_cbl/OUTPUT/e1_cbl_3d.000.nc'
ds = xr.open_dataset(filename)
coarsen_factor = 10
uda_coarse = ds['u'].coarsen(xu=coarsen_factor, y=coarsen_factor).mean()
vda_coarse = ds['v'].coarsen(x=coarsen_factor, yv=coarsen_factor).mean()
#%%
with plt.style.context(['science', 'no-latex']):
    fig, axes = plt.subplots(1, 2, dpi=100, figsize=(11, 4))
    plt.subplots_adjust(wspace=0.3, hspace=0.2, right=0.92, top=0.95, left=0.1)

    # Contour plot
    cs = ds['theta'][-1, 10, :, :].plot.contourf(
        ax=axes[0],
        robust=True,
        cmap='jet',
        add_colorbar=True,
    )

    # Quiver plot
    quiver = axes[0].quiver(ds['x'][::coarsen_factor], ds['y'][::coarsen_factor],
                            uda_coarse[-1, 10, :, :], vda_coarse[-1, 10, :, :], scale=50)

    # Quiver key
    qk = plt.quiverkey(quiver, 0.9, -0.09, 1, r'$1$ $m/s$', labelpos='E',
                       coordinates='axes', fontproperties={'weight': 'bold'})
    axes[0].plot([0,2000],[1502.5,1502.5],lw=3,color='r')
    # Other settings and formatting
    title = ('Plot of ' + ds['theta'].attrs.get('long_name', None)
             + ' ' * 3
             + 't=' + axes[0].get_title()[14:16] + 'h   '
             + 'z=' + axes[0].get_title()[-11:-6] + 'm'
             + ' ' * 6
             + ds['theta'].attrs.get('units', None))
    axes[0].set_title(title)
    axes[0].set_ylim(0, 2000)
    axes[0].set_yticks(np.arange(300, 2000, 300))
    axes[0].set_xlim(0, 2000)
    axes[0].set_xticks(np.arange(300, 2000, 300))
    
    cs = ds['w'][-1, :, :, 300].plot.contourf(
        ax=axes[1],
        robust=True,
        cmap='jet',
        add_colorbar=True,
    )
    title = ('Plot of ' + ds['w'].attrs.get('long_name', None)
             + ' ' * 3
             + 't=' + axes[1].get_title()[14:16] + 'h   '
             + 'y=1502.5m'
             + ' ' * 6
             + ds['w'].attrs.get('units', None))
    axes[1].set_title(title)
    axes[1].set_ylabel('z [meters]')
    axes[1].plot([0,2000],[47.5,47.5],lw=3,color='r')
    # axes[0].set_ylim(0, 3000)
    axes[1].set_yticks(np.arange(500, 3200, 500))
    axes[1].set_xlim(0, 2000)
    axes[1].set_xticks(np.arange(300, 2000, 300))

plt.show()
plt.savefig('../e1_cbl/OUTPUT/xy_theta_z_t_w.png')

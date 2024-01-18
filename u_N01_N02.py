#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:01:47 2024

@author: zhang
"""

import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np

# Load datasets
ds_3d_av_N01 = xr.open_dataset('../OUTPUT/Tokyo_LSM_av_3d.000.nc')
ds_3d_av_N02 = xr.open_dataset('../OUTPUT/Tokyo_LSM_av_3d_N02.000.nc')

# Create subplots
fig, ax = plt.subplots(dpi=140, figsize=(5.5, 4.5))
plt.subplots_adjust(right=0.92, top=0.95, left=0.12)

# Plot ds_3d_av_N01 in the upper left quadrant
cs1 = ds_3d_av_N01['theta'][-10, 10, :, :].plot.imshow(
    ax=ax,
    robust=True,
    cmap='jet',
    add_colorbar=True,
    vmin = 295,
    vmax = 295.4
)
# coarsen_factor = 8
# uda_coarse = ds_3d_av_N01['u'].coarsen(xu=coarsen_factor, y=coarsen_factor).mean()
# vda_coarse = ds_3d_av_N01['v'].coarsen(x=coarsen_factor, yv=coarsen_factor).mean()
# # Quiver plot
# quiver = ax.quiver(ds_3d_av_N01['x'][::coarsen_factor], ds_3d_av_N01['y'][::coarsen_factor],
#                         uda_coarse[-1, 10, :, :], vda_coarse[-1, 10, :, :], scale=50)

# # Quiver key
# qk = plt.quiverkey(quiver, 0.9, -0.09, 1, r'$1$ $m/s$', labelpos='E',
#                    coordinates='axes', fontproperties={'weight': 'bold'})
ax.set_title(' ')
ax.set_yticks(np.arange(1600,10000,2560))
ax.set_xticks(np.arange(1600,10000,2560))
# title = ('Plot of ' + ds_3d_av_N01['theta'].attrs.get('long_name', None)
#          + ' ' * 3
#          + 't=' + ax.get_title()[14:16] + 'h   '
#          + 'z' + ax.get_title()[-11:-5] + 'm'
#          + ' ' * 6
#          + ds_3d_av_N01['theta'].attrs.get('units', None))
# ax.set_title(title)

# Create inset axes for ds_3d_av_N02
# axins = inset_axes(ax, width="50%", height="50%", bbox_to_anchor=(1.1, 0.5, 0.5, 0.5), bbox_transform=ax.transAxes)
in_ax = fig.add_axes([0.22, 0.2415, 0.32, 0.420]) 
# in_ax = fig.add_axes([0.12, 0.2415, 0.32, 0.420]) 

in_ax.spines['right'].set_visible(False)
in_ax.spines['bottom'].set_visible(False)
in_ax.spines['left'].set_visible(False)
in_ax.spines['top'].set_visible(False)
# ax1.tick_params(axis='x',which='minor',direction= 'out', length=2)
# ax1.tick_params(axis='x',which='major',direction= 'out', length=4)
in_ax.get_yaxis().set_visible(False)
in_ax.get_xaxis().set_visible(False)



# Plot ds_3d_av_N02 in the lower right quadrant with adjusted extent
cs2 = ds_3d_av_N02['theta'][-10, 40, :, :].plot.imshow(
    ax=in_ax,
    robust=True,
    cmap='jet',
    add_colorbar=False,
    vmin = 295,
    vmax = 295.4
)
in_ax.set_xlabel(' ')
in_ax.set_ylabel(' ')
in_ax.set_title(' ')
ax.plot([1600,1600],[1600,6720],lw=3,color='k')
ax.plot([1600,6720],[6720,6720],lw=3,color='k')
ax.plot([6720,6720],[1600,6720],lw=3,color='k')
ax.plot([1600,6720],[1600,1600],lw=3,color='k')
ax.text(150,9800,'D1',fontdict = {'weight': 'bold', 'size': 10})
in_ax.text(150,4800,'D2',fontdict = {'weight': 'bold', 'size': 10})
in_ax.scatter(2560,2560,s=20,marker='*',color='w')
plt.savefig('../xy_theta.png')

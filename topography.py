#!/usr/bin/python3

''' It produces plots of topography for 0.44, 0.11 and 0.03 '''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset


filename = ['topo0.44_EUROPE.nc','topo0.11_EUROPE.nc', 'topo0.03_ALPS.nc']
var = ['50', '12', '3']
path = '/home/irida/Downloads/'


for i in range(3):
    
    fullname = path + filename[i]
    
    # read data
    data = Dataset(fullname, 'r')
    topo = data.variables['HGT_M'][0,:,:]
    lat = data.variables['XLAT_M'][0,:,:]
    lon = data.variables['XLONG_M'][0,:,:]

    # ------------------------
    # plots
    fig = plt.figure(figsize=(8,5))
    map = Basemap(llcrnrlon=1., urcrnrlon=17., llcrnrlat=40., urcrnrlat=50., resolution='l')
    parallels = np.arange(40., 50.1, 5)
    meridians = np.arange(0., 17., 5)
    
    map.drawparallels(parallels, labels=[1,0,0,0], fontsize=6, linewidth=0.5, dashes=[2,2])
    map.drawmeridians(meridians, labels=[0,0,0,1], fontsize=6, linewidth=0.5, dashes=[2,2])
    map.drawcoastlines(linewidth=0.5)
   
    map.drawmapboundary(linewidth=0.5)
    bounds = np.arange(0, 4000, 200)
    ticks =  np.arange(0, 4000, 200)
    
   
    contour = map.contourf(lon, lat, topo[:,:], levels=bounds,  cmap='terrain', extend='max')
    cbar = map.colorbar(contour, ticks=ticks, pad='5%')
    cbar.set_label('m', rotation=0, labelpad=8, fontsize=7)
    cbar.ax.tick_params(labelsize=6)
         
    plt.title(var[i]+ ' Km', fontsize=12, y=1.02)
    plt.savefig('topo_'+var[i]+'km'+'.png', bbox_inches='tight', dpi=300)
      
    plt.close()
    

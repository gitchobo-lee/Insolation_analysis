import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
path = "C:/Users/lhkjo/Downloads/KMAP_latlon.nc"
fdata=nc.Dataset(path)
print(fdata)
print(fdata['latitude'][0,0])
print(fdata['latitude'][6749,0])
print(fdata['longitude'][6749,0])
print(fdata['longitude'][6749,6899])
#long = fdata['X'][100:4600].data
#lat = fdata['Y'][100:4000].data
#SWDN = fdata['SWDN_flat_with_shading'][100:4000,100:4600].data
#print(type(SWDN), np.shape(SWDN))
#
#fig,ax = plt.subplots()
#qq = ax.pcolor(long,lat,SWDN[:],cmap='jet')
#cbar = fig.colorbar(qq)
#cbar.set_label('surface temp')
#plt.show()
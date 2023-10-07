import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patches as patches
path = "C:/Users/lhkjo/Downloads/KMAPP_solar_FWS_total_mean.nc"
fdata=nc.Dataset(path)
long_pre = fdata['X'][:].data #6900 - 가로축값, column
lat_pre = fdata['Y'][:].data #6750 - 세로축값, row
long_count = int(len(long_pre)/10)
lat_count = int(len(lat_pre)/10)
df = pd.DataFrame(index=range(lat_count),columns=range(long_count))
df.fillna(0,inplace=True)
print(df.shape) #(row,column) - (675,690)
SWDN = fdata['SWDN_flat_with_shading'][:].data
for i in range(0,lat_count):
    for j in range(0,long_count):
        df.at[i,j]=np.mean(SWDN[i*10:i*10+10,j*10:j*10+10])
        
df.to_csv("./summarized_data.csv")
fig,ax = plt.subplots()
qq=ax.pcolor(range(0,675),range(lat_count),df.iloc[:,0:675],cmap='jet')
cbar = fig.colorbar(qq)
cbar.set_label('surface temp')
ax.add_patch(
    patches.Rectangle(
        (281-25,147-22),
        50,44,
        edgecolor='blue',
        facecolor='#A9E2F3',
        fill=True,
    )
)
plt.show()

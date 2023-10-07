import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

raw_data = pd.read_csv("./summarized_data.csv",sep=",")
real_data = raw_data.iloc[:,1:]
window_width = 38
window_height= 40
iteration = 0
max_value = 0
max_value_iter = 0
for i in range(0,675-window_height): # 675 - 세로축수, row수
    for j in range(0,690-window_width): # 690 - 가로축수, column수
        average = np.mean(real_data.iloc[i:i+window_height,j:j+window_width])
        iteration += 1
        if (max_value < average):
            max_value = average
            max_value_iter = iteration
            print(iteration, max_value)
fig,ax = plt.subplots()
qq=ax.pcolor(range(0,675),range(0,675),real_data.iloc[:,0:675],cmap='jet')
cbar = fig.colorbar(qq)
cbar.set_label('surface temp')
ax.add_patch(
    patches.Rectangle(
        ((max_value_iter%(690-window_width))-(window_width//2),(max_value_iter//(690-window_width))-(window_height//2)),
        window_width,window_height,
        edgecolor='blue',
        facecolor='#A9E2F3',
        fill=True,
    )
)
plt.show()

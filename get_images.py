import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt


#load pickle file csDataframe.pkl
with open('./csDataframe.pkl', 'rb') as f:
    data = pickle.load(f)
nparr = []
count = 0
for row in data.itertuples():
    print(count)

    y, sr = row.npArr, 4000

    def make_image(data, outputname, size=(1, 1), dpi=80):
        fig = plt.figure()
        ax = plt.Axes(fig, [0., 0., 1., 1.])
        ax.set_axis_off()
        fig.add_axes(ax)
        plt.set_cmap('hot')

        time2 = np.linspace(
            0, # start
            len(y)/sr,
            num = len(data)
        )
        ax.plot(time2, data)
        plt.savefig(outputname, dpi=dpi)
        plt.clf()
        fig.clf()

    # data = mpimg.imread(inputname)[:,:,0]
    data = np.arange(1,10).reshape((3, 3))

    make_image(y, f'./soundWaveFigs/Segment of {row.File_Name} at {row.Start} to {row.End}.png')

    count+=1





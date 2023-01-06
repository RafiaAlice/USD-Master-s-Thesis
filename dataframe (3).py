import pandas as pd
import numpy as np
import librosa
import pickle
import matplotlib.pyplot as plt


data = pd.read_csv('./Split_Sound.csv')


nparr = []
count = 0
for row in data.itertuples():
    print(count)

    

    y, sr = librosa.load('./ICBHI_final_database/' + row.File_Name + '.wav', sr = 4000)

    xarr = np.zeros(12031)

    y = y[int(row.Start*sr):int(row.End*sr)]

    for i in range(len(y)):
        if (i > 12030):
            break
        xarr[i] = y[i]
    
    nparr.append(xarr)



    time2 = np.linspace(
        0, # start
        len(y)/sr,
        num = len(y)
    )

    
    plt.plot(time2,y)

    plt.savefig(f'./soundWaveFigs/Segment of {row.File_Name} at {row.Start} to {row.End}.png', dpi=250)
    plt.clf()

    count+=1


data['npArr'] = nparr

# abspath = pathlib.Path(filename).absolute()
# with open(str(abspath), 'wb') as f:
#     pickle.dump(thing_to_pickle, f)

pickle.dump(data, open('./csDataframe.pkl', 'wb'))



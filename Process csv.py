import pandas as pd 
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_file', type=str)
args = parser.parse_args()

df = pd.read_csv(args.input_file, header=None)
y = df[1].tolist()
x = df[0].tolist()
plt.plot(x,y)
plt.xlabel('Frequency (kHz)')
plt.ylabel('Amplitude (V)')

y2 = savgol_filter(y, 1111, 5)
plt.figure()
plt.plot(x, y2)
plt.xlabel('Frequency (kHz)')
plt.ylabel('Amplitude (V)')

plt.show()

def local_maxima(seq):
    candidate = False
    i = None
    for index, elem in enumerate(seq):
        
        if i is None:
            i = elem
            candidate = True
        elif elem > i:
            i = elem
            candidate = True
        elif elem == i:
            candidate = False
        elif elem < i:
            if candidate and elem > 10:
                yield index, i
            i = elem
            candidate = False

new_y_list = [i for i in y2 if i > 10]
maxima = list(local_maxima(y2))

index = [i[0] for i in maxima]
peak_freq = [x[j] for j in index]
print(peak_freq)
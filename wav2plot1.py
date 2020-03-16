#!/usr/bin/python3

import scipy
from scipy.io import wavfile
import numpy as np
import utils

import matplotlib.pyplot as plt
import matplotlib.animation as animation

FPS = 30
plt.style.use('dark_background')
fig, ax = plt.subplots()
fw = animation.FFMpegWriter(FPS)
fig.set_size_inches(192, 27)

sample_rate, data = wavfile.read('alone.wav')
mono = (data.T[0] + data.T[1]) / 2.0 # average stereo into mono
secs = int(len(mono) / sample_rate)+1
spf = int(sample_rate / FPS)
q = sample_rate / spf

with fw.saving(fig, "plot1.mp4", 10):
    for frame in range(secs * FPS):
        ax.clear()
        ax.axis('off')
        ax.set_ylim(0, 150000)

        # FFT, process data
        slot = mono[frame*spf:(frame+1)*spf]
        fourier = np.abs(np.fft.fft(slot, norm="ortho"))[:100]
        fourier[fourier < 20000] = 0
        print(frame)
        ax.bar(range(len(fourier)), fourier, color="red")
        fw.grab_frame()

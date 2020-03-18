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
#mono = (data.T[0] + data.T[1]) / 2.0 # average stereo into mono
left = data.T[0]
right = data.T[1]
secs = int(len(left) / sample_rate)+1
spf = int(sample_rate / FPS)
q = sample_rate / spf

with fw.saving(fig, "plot2.mp4", 14):
    for frame in range(secs * FPS):
        print(frame)
        ax.clear()
        ax.axis('off')
        ax.set_ylim(-30000, 30000)

        #slot_mono = mono[frame*spf:(frame+1)*spf]
        slot_left = left[frame*spf:(frame+1)*spf]
        slot_right = right[frame*spf:(frame+1)*spf]
        #ax.plot(slot_mono, color="green", linewidth=2)
        ax.plot(slot_left, color="blue", linewidth=20)
        ax.plot(slot_right, color="yellow", linewidth=20)
        #plt.pause(1/10)
        fw.grab_frame()

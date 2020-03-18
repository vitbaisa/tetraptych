#!/usr/bin/python3

import scipy
from scipy.io import wavfile
import numpy as np
from PIL import Image

FPS = 30
sample_rate, data = wavfile.read('alone.wav')
mono = (data.T[0] + data.T[1]) / 2.0 # average stereo into mono
secs = int(len(mono) / sample_rate)+1
spf = int(sample_rate / FPS)

image = Image.new("RGBA", (secs*FPS, 270), (0, 0, 0, 255))
pixels = image.load()

for frame in range(secs * FPS):
    print(frame)
    slot = mono[frame*spf:(frame+1)*spf]
    if not len(slot):
        break
    fourier = np.abs(np.fft.fft(slot))
    fourier *= 255/fourier.max()
    for i, peak in enumerate(fourier[:135]):
        p = int(peak)
        pixels[frame, 2*i] = (p, p, p, 255)
        pixels[frame, 2*i+1] = (p, p, p, 255)

image.save("spectrum2.png")

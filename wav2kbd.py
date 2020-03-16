#!/usr/bin/python3

import scipy
import cairo
from scipy.io import wavfile
import numpy as np
import utils
from xml.dom import minidom

imagesize = (1920, 270)
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, *imagesize)
c = cairo.Context(surface)
ff = utils.Video(1920, 270, 30, "kbd.mp4")

import gi
gi.require_version('Rsvg', '2.0')
from gi.repository import Rsvg

pno = [27.5000, 29.1353, 30.8677, 32.7032, 34.6479, 36.7081,
        38.8909, 41.2035, 43.6536, 46.2493, 48.9995, 51.9130, 55.0000, 58.2705,
        61.7354, 65.4064, 69.2957, 73.4162, 77.7817, 82.4069, 87.3071, 92.4986,
        97.9989, 103.826, 110.000, 116.541, 123.471, 130.813, 138.591, 146.832,
        155.563, 164.814, 174.614, 184.997, 195.998, 207.652, 220.000, 233.082,
        246.942, 261.626, 277.183, 293.665, 311.127, 329.628, 349.228, 369.994,
        391.995, 415.305, 440.000, 466.164, 493.883, 523.251, 554.365, 587.330,
        622.254, 659.255, 698.456, 739.989, 783.991, 830.609, 880.000, 932.328,
        987.767, 1046.50, 1108.73, 1174.66, 1244.51, 1318.51, 1396.91, 1479.98,
        1567.98, 1661.22, 1760.00, 1864.66, 1975.53, 2093.00, 2217.46, 2349.32,
        2489.02, 2637.02, 2793.83, 2959.96, 3135.96, 3322.44, 3520.00, 3729.31,
        3951.07, 4186.01]

scale = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

def fridx2tone(i):
    return "%s:%d" % (scale[i % 12], i//12-3)

def fr2tone(fr):
    l = 0
    r = len(pno)
    p = (l+r) // 2
    while p > 0 and p < len(pno) and r-l > 1:
        if fr < pno[p]:
            r = p
        elif fr > pno[p]:
            l = p
        p = (l+r) // 2
    if p > 0 and abs(pno[p-1]-fr) < abs(pno[p]-fr):
        return p-1
    if p < len(pno)-1 and abs(pno[p+1]-fr) < abs(pno[p]-fr):
        return p+1
    return p

FPS = 30
sample_rate, data = wavfile.read('alone.wav')
mono = (data.T[0] + data.T[1]) / 2.0 # average stereo into mono
secs = int(len(mono) / sample_rate)+1
spf = int(sample_rate / FPS)
q = sample_rate / spf
svgdom2 = minidom.parse("kbd2.svg").documentElement

for frame in range(secs * FPS):
    # FFT, process data
    slot = mono[frame*spf:(frame+1)*spf]
    fourier = np.abs(np.fft.fft(slot, norm="ortho"))[:50]
    fourier[fourier < 20000] = 0
    topf = np.sort(fourier)[::-1][:8]
    sorted_indices = np.argsort(fourier)[::-1][:8]
    real_freqs = [x*q for x in sorted_indices if fourier[x] > 0.0]
    tones = [fr2tone(x) for x in real_freqs]
    print(frame)

    # svg
    c.set_source_rgb(0, 0, 0)
    c.paint()
    old_attrs = []
    for k in set(tones):
        rects = svgdom2.getElementsByTagName('rect')
        for r in rects:
            if r.getAttribute('id') == "%d" % k:
                old_attrs.append((r, r.getAttribute('style')))
                r.setAttribute('style', 'fill:red;stroke:black')
    handle = Rsvg.Handle()
    kbd = handle.new_from_data(bytes(svgdom2.toxml(), "utf-8"))
    kbd.render_cairo(c)
    ff.write_frame(surface.get_data().tobytes())
    for k, v in old_attrs:
        k.setAttribute('style', v)

ff.finish()

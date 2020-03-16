import random
import math
import requests
import subprocess

def hex2rgb(s):
    s = s.lstrip('#').rstrip(';')
    return int(s[:2], 16)/255, int(s[2:4], 16)/255, int(s[4:6], 16)/255

def hexagonal_grid():
    # obrazek: https://www.instagram.com/p/B0LjLChHr_z/
    # teorie: https://www.redblobgames.com/grids/hexagons/
    pass

class Video():
    def __init__(self, width=1920, height=1080, fps=30, output_file="out.mp4"):
        self.width = width
        self.height = height
        self.fps = fps
        command = [
            "ffmpeg",
            '-y',  # overwrite output file if it exists
            '-f', 'rawvideo',
            '-s', '%dx%d' % (width, height),  # size of one frame
            '-pix_fmt', 'bgra',
            '-r', str(fps),  # frames per second
            '-i', '-',  # The input comes from a pipe
            '-c:v', 'h264_nvenc',
            '-an',  # Tells FFMPEG not to expect any audio
            '-loglevel', 'error',
            '-vcodec', 'libx264',
            '-pix_fmt', 'yuv420p',
            output_file
        ]
        self.process = subprocess.Popen(command, stdin=subprocess.PIPE)

    def write_frame(self, data):
        self.process.stdin.write(data)

    def finish(self):
        self.process.stdin.close()
        self.process.wait()

    def __del__(self):
        self.finish()


def parse_parameters(sysargv, settings):
    params = list(sysargv)
    for p in settings.keys():
        if ('--'+p) in params:
            i = params.index('--'+p)
            del params[i]
            if type(settings[p]) == type(0):
                settings[p] = int(params[i])
            elif type(settings[p]) == type(0.0):
                settings[p] = float(params[i])
            else:
                settings[p] = params[i]
            del params[i]

def thesaurus(lemma='', lpos=''):
    skell_url = "https://skell.sketchengine.co.uk/run.cgi/thesaurus?lpos=%s&query=%s&format=json"
    return [x["word"] for x in requests.get(skell_url % (lpos, lemma)).json().get('Words', [])]

def triangle_orientation(a, b, c):
    t1 = (abs(a[0]-b[0]), abs(a[1]-b[1]))
    t2 = (abs(b[0]-c[0]), abs(b[1]-c[1]))
    t3 = (abs(c[0]-a[0]), abs(c[1]-a[1]))
    return (t1[0]+t2[0]+t3[0]/3.0, t1[1]+t2[1]+t3[1]/3.0)

def get_quadrant(point):
    if point[0] == point[1] and point[0] == 0:
        return 0
    if point[0] > 0:
        if point[1] > 0:
            return 1
        else:
            return 4
    else:
        if point[1] > 0:
            return 2
        else:
            return 3

def d(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def filter_close_points(points, dist=10):
    i = 0
    while i < len(points)-1:
        j = i + 1
        while j < len(points):
            if d(points[i], points[j]) < dist:
                del points[j]
            else:
                j += 1
        i += 1
    return points

def inSortedList(w):
    start = 0
    end = len(enwl2) - 1
    middle = (start + end) // 2
    while start+1 < end:
        if enwl2[middle] == w:
            return True
        elif enwl2[middle] < w:
            start = middle
        else:
            end = middle
        middle = (start + end) // 2
    return False

def englishRandomLetter():
    chars = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    probs = [8.167, 0.01492, 2.782, 4.253, 12.702, 2.228, 2.015,
        6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929,
        0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974,
        0.074]
    return random.choices(chars, probs)

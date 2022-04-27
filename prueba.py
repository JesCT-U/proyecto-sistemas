from email.mime import audio
import numpy as np
import soundfile as sf
import sounddevice as sd



def reflejar():
    s, fs = sf.read("C:/Users/jesus/Desktop/PJ.wav", dtype='float32')
    nn = s[ : : -1]
    sd.play(nn, fs)
    sd.wait()


def intercambiar():
    n, fs = sf.read("C:/Users/jesus/Desktop/The Weeknd - Until I Bleed Out.flac")

    ffs = 0
    fss = 0

    longitud = len(n)

    for x in range(0,longitud):
        for y in [0,1]:
            if y == 0:
                ffs = n[x,y]
            else:
                fss = n[x,y]

        n[x,0] = fss
        n[x,1] = ffs

    sd.play(n, fs)
    sd.wait()

def amplitud():

    n, fs = sf.read("C:/Users/jesus/Desktop/PJ.wav", dtype='float32')

    valor = -5

    n = np.multiply(n,valor)

    sd.play(n, fs)
    sd.wait()

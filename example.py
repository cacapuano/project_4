# example code for FFT project

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq # our project is based around fft

def signal(): # import signal over here
    data = np.loadtxt() # load data file
    time = data[]
    signal = 
    return time, signal

def use_fft(time, signal):
    N = len(signal) # length of signal = number of data pts
    dt = time[1]-time[0] # time interval
    yf = fft(signal)
    xf = fftfreq(N, dt)[] # compute frequencies

    # plot signal
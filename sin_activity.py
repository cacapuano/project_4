#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Parameters
sampling_rate = 1000  # Resolution
duration = 1  # How long you want the wave to continue
# Determine your frequency
frequency = 
amplitude = 1  
phase = 0  

# Time
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# MISSING SECTION - generate signal, then apply fft and fftfreq
# Generate the continuous sinusoidal signal
signal = 

# Apply FFT
fft_result = 
fft_freqs = 

# Get the magnitude of the FFT (only positive frequencies)
fft_magnitude = np.abs(fft_result)
positive_freqs = fft_freqs[:len(fft_freqs)//2]
positive_magnitude = fft_magnitude[:len(fft_magnitude)//2]

# Create dataset (time vs signal, frequency vs fft magnitude)
time_data = np.column_stack((t, signal))  # Time-domain signal
frequency_data = np.column_stack((positive_freqs, positive_magnitude))  # Frequency-domain data (positive frequencies)

# Display the data
plt.figure(figsize=(10, 6))

# Time-domain plot
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Continuous Sinusoidal Wave (Time Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Frequency-domain plot
plt.subplot(2, 1, 2)
plt.plot(positive_freqs, positive_magnitude)
plt.title("FFT of Continuous Sinusoidal Wave (Frequency Domain)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.tight_layout()
filename = f'sinusoidal_fft_{frequency}Hz.png'
plt.savefig(filename)

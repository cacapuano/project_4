#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Parameters
sampling_rate = 1000  # Samples per second
duration = 1  # Duration in seconds
frequency = 50  # Frequency of the sinusoidal wave in Hz
amplitude = 1  # Amplitude of the wave
phase = 0  # Phase shift (in radians)

# Time vector
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
plt.savefig('sinusodal_fft.png')

# Output data for inspection
time_data[:10], frequency_data[:10]  # Display the first 10 rows of each dataset

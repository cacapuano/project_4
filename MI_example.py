#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Parameters
sampling_rate = 1000  # Samples per second
duration = 1  # Duration in seconds
interferometer_freq = 10  # Frequency of the interferometer signal in Hz (modulation frequency)
noise_amplitude = 0.5  # Amplitude of the Gaussian noise

# Time vector
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Ideal Interferometer Signal: A sinusoidal signal with frequency `interferometer_freq`
ideal_signal = np.cos(2 * np.pi * interferometer_freq * t)

# Add Gaussian Noise
noise = noise_amplitude * np.random.randn(len(t))

# Total Signal = Ideal Signal + Noise
total_signal = ideal_signal + noise

# Apply FFT
fft_result = np.fft.fft(total_signal)
fft_freqs = np.fft.fftfreq(len(t), 1/sampling_rate)

# Get the magnitude of the FFT (only positive frequencies)
fft_magnitude = np.abs(fft_result)
positive_freqs = fft_freqs[:len(fft_freqs)//2]
positive_magnitude = fft_magnitude[:len(fft_magnitude)//2]

# Create dataset (time vs signal, frequency vs fft magnitude)
time_data = np.column_stack((t, total_signal))  # Time-domain signal
frequency_data = np.column_stack((positive_freqs, positive_magnitude))  # Frequency-domain data (positive frequencies)

# Display the data
plt.figure(figsize=(10, 6))

# Time-domain plot
plt.subplot(2, 1, 1)
plt.plot(t, total_signal)
plt.title("Michelson Interferometer Signal with Noise (Time Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Frequency-domain plot
plt.subplot(2, 1, 2)
plt.plot(positive_freqs, positive_magnitude)
plt.title("FFT Magnitude of Interferometer Signal (Frequency Domain)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.savefig('MI_example.png')

# Output data for inspection
time_data[:10], frequency_data[:10]  # Display the first 10 rows of each dataset

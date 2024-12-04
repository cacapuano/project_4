#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Parameters
sampling_rate = 1000  # Samples per second
duration = 1  # Duration in seconds

# Frequencies and amplitudes of the sinusoidal waves
frequencies = [50, 120, 200]  # Frequencies in Hz
amplitudes = [1, 0.5, 0.7]  # Amplitudes of the waves
phases = [0, np.pi/4, np.pi/2]  # Phase shifts of the waves

# Time vector
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the composite signal by summing sinusoidal waves
composite_signal = np.sum([amplitude * np.sin(2 * np.pi * frequency * t + phase) 
                           for amplitude, frequency, phase in zip(amplitudes, frequencies, phases)], axis=0)

# Apply FFT to the composite signal
fft_result = np.fft.fft(composite_signal)
fft_freqs = np.fft.fftfreq(len(t), 1/sampling_rate)

# Get the magnitude of the FFT (only positive frequencies)
fft_magnitude = np.abs(fft_result)
positive_freqs = fft_freqs[:len(fft_freqs)//2]
positive_magnitude = fft_magnitude[:len(fft_magnitude)//2]

# Create dataset (time vs signal, frequency vs fft magnitude)
time_data = np.column_stack((t, composite_signal))  # Time-domain signal
frequency_data = np.column_stack((positive_freqs, positive_magnitude))  # Frequency-domain data (positive frequencies)

# Display the data
plt.figure(figsize=(10, 6))

# Time-domain plot
plt.subplot(2, 1, 1)
plt.plot(t, composite_signal)
plt.title("Combination of Sinusoidal Waves (Time Domain)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

# Frequency-domain plot
plt.subplot(2, 1, 2)
plt.plot(positive_freqs, positive_magnitude)
plt.title("FFT of Combined Sinusoidal Waves (Frequency Domain)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.savefig('combined.png')

# Output data for inspection
time_data[:10], frequency_data[:10]  # Display the first 10 rows of each dataset

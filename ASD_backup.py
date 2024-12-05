#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks

# Step 1: Ask the user for the file path and name
file_path = input("Enter the path to your data file (e.g., /path/to/data.lvm): ")

# Extract the file name from the file path
file_name = os.path.basename(file_path)

# Step 2: Load the LVM file (assuming it's a text file with the columns you mentioned)
# Update the separator if needed (default is tab-separated)
try:
    data = pd.read_csv(file_path, sep='\t', comment=';', header=None, names=['Time(s)', 'polarized_x_a', 'polarized_y_a', 'polarized_x_b', 'polarized_y_b'])
    print("Data successfully loaded.")
except Exception as e:
    print(f"Error loading the file: {e}")
    exit()

# Step 3: Extract relevant columns
time = data['Time(s)'].values
polarized_x_a = data['polarized_x_a'].values
polarized_y_a = data['polarized_y_a'].values
polarized_x_b = data['polarized_x_b'].values
polarized_y_b = data['polarized_y_b'].values

# Step 4: Sampling rate and time step
dt = time[1] - time[0]  # time difference between consecutive data points
sampling_rate = 1 / dt   # sampling rate in Hz

# Step 5: Perform FFT on the data
# We will use one of the signals, here polarized_x_a as an example
signal = polarized_x_a

# Apply FFT
N = len(signal)  # Number of points
freq = fftfreq(N, dt)  # Frequency array
fft_signal = fft(signal)  # Perform FFT

# Step 6: Compute the Amplitude Spectral Density (ASD)
# ASD is the square root of the Power Spectral Density (PSD)
psd = np.abs(fft_signal)**2 / N  # Power Spectral Density
asd = np.sqrt(psd)  # Amplitude Spectral Density

# Step 7: Prompt the user to enter a custom threshold
threshold_input = input(f"Enter the threshold for peak detection as a fraction of the maximum ASD (e.g., 0.1 for 10% of max ASD): ")

try:
    threshold_fraction = float(threshold_input)
    if threshold_fraction < 0 or threshold_fraction > 1:
        print("Threshold fraction must be between 0 and 1. Setting to default 10% (0.1).")
        threshold_fraction = 0.1  # Default to 10% if the input is out of range
except ValueError:
    print("Invalid input. Setting threshold to 10% of the maximum ASD.")
    threshold_fraction = 0.1  # Default to 10% if the input is invalid

# Calculate the threshold value based on the user-defined fraction of the maximum ASD
threshold = threshold_fraction * np.max(asd)

print(f"Using threshold: {threshold:.2f} m/√Hz")

# Step 8: Identify frequency peaks using the threshold
peaks, _ = find_peaks(asd[:N//2], height=threshold)  # Find peaks above the user-defined threshold

# Step 9: Plot the ASD with peaks highlighted
plt.figure(figsize=(10, 6))
plt.loglog(freq[:N//2], asd[:N//2])  # Plot only the positive frequencies (real part)

# Highlight the identified peaks
plt.scatter(freq[peaks], asd[peaks], color='red', label='Frequency Peaks', zorder=5)

# Labeling the axes with the appropriate units
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude Spectral Density (m/√Hz)')  # The units for ASD
plt.title(f'FFT Plot of {file_name}')  # Title with the file name
plt.grid(True)

# Show the legend for the peaks
plt.legend()

# Save the plot as a PNG image
plt.savefig(f'FFT Plot of {file_name}.png')
print('Plotted FFT successfully!')

# Optionally, print out the identified peaks and their corresponding frequencies
if len(peaks) > 0:
    print(f"Identified peaks at the following frequencies (Hz):")
    for peak in peaks:
        print(f"Frequency: {freq[peak]:.2f} Hz, ASD: {asd[peak]:.2f} m/√Hz")
else:
    print("No significant peaks found above the threshold.")

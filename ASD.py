#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

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

# Step 7: Plot the ASD with units
plt.figure(figsize=(10, 6))
plt.loglog(freq[:N//2], asd[:N//2])  # Plot only the positive frequencies (real part)

# Labeling the axes with the appropriate units
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude Spectral Density (m/√Hz)')  # The units for ASD
plt.title(f'FFT Plot of {file_name}')  # Title with the file name
plt.grid(True)

# Show the plot
plt.savefig(f'FFT Plot of {file_name}.png')
print('Plotted FFT successfully!')

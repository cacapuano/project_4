# read me file
Practice with a sinusodal function

1. Generate the continuous sinusoidal signal

`signal = amplitude * np.sin(2 * np.pi * frequency * t + phase)`

2. Apply FFT
fft_result = np.fft.fft(signal)
fft_freqs = np.fft.fftfreq(len(t), 1/sampling_rate)

3. Get the magnitude of the FFT (only positive frequencies)
fft_magnitude = np.abs(fft_result)
positive_freqs = fft_freqs[:len(fft_freqs)//2]
positive_magnitude = fft_magnitude[:len(fft_magnitude)//2]

4. Create dataset (time vs signal, frequency vs fft magnitude)
time_data = np.column_stack((t, signal))  # Time-domain signal
frequency_data = np.column_stack((positive_freqs, positive_magnitude))  # Frequency-domain data (positive frequencies)

# README.md

## SciPy.fft or Numpy.fft
Using ```fft``` and ```fftfreq``` is a great way to convert your data from the time domain to the frequency domain.

## In-class Activity
Practice with a sinusodal function. 

1. Generate the continuous sinusoidal signal

```
signal = amplitude * np.sin(frequency * t + phase)
```

2. Apply FFT

```
fft_result = np.fft.fft(__)
```

```
fft_freqs = np.fft.fftfreq(__)
```

4. Get the magnitude of the FFT (only positive frequencies)

```
fft_magnitude = np.abs(fft_result)
```

```
positive_freqs = fft_freqs[:len(fft_freqs)//2]
```

```
positive_magnitude = fft_magnitude[:len(fft_magnitude)//2]
```

5. Create dataset (time vs signal, frequency vs fft magnitude)

`time_data = np.column_stack((t, signal))  # Time-domain signal`

`frequency_data = np.column_stack((positive_freqs, positive_magnitude))  # Frequency-domain data (positive frequencies)`

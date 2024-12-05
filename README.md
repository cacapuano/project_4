# README.md

## SciPy.fft or Numpy.fft
Using ```fft``` and ```fftfreq``` is a great way to convert your data from the time domain to the frequency domain.

## In-class Activity
Practice with a sinusodal function. 

Setting-up the environment
1. ```
   mkdir FFT
   ```
2. ```
   git clone https://github.com/cacapuano/project_4.git
   ```
3. Open```sin_activity.py```


Practice with a known function

1. Generate the continuous sinusoidal signal

```
function = amplitude * np.sin(frequency * t + phase)
```

2. Apply FFT

Put the correct argument (__) using the documentation 

(https://numpy.org/doc/2.1/reference/generated/numpy.fft.fft.html#numpy.fft.fft)

```
fft_result = np.fft.fft(__)
```

Plug in the correct argument (__) using the documentation 

(https://docs.scipy.org/doc/scipy/reference/generated/scipy.fft.fftfreq.html)

```
fft_freqs = np.fft.fftfreq(__)
```

3. Run ```sin_activity.py```
4. Check if the fft plot has the corresponding frequency you entered. 

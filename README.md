# README.md

## SciPy.fft / Numpy.fft
Using ```fft``` and ```fftfreq``` is a great way to convert your data from the time domain to the frequency domain.

## In-class Activity - Part I
Practice with a known sinusodal function. 

Setting-up the environment: 
1. ```
   mkdir FFT
   ```
2. ```
   cd FFT
   ```
3. ```
   git clone https://github.com/cacapuano/project_4.git
   ```
4. ```
   cd project_4
   ```
5. Open```sin_activity.py```


Find the lines that are missing: 

1. Generate the continuous sinusoidal signal

```
function = amplitude * np.sin(2*np.pi*frequency * t + phase)
```
***Don't forget the 2π, because ω = 2π ⋅ frequency.***

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

3. Make the file excutable: 
```
chmod +x sin_activity.py
```
4. Run ```sin_activity.py```
5. Check if the fft plot has the corresponding frequency you entered.


## In-class Activity - Part II

Practice with a more complex known sinusodal function. 
You can do either: 
- Open```sin_activity.py```
- Create a function of a combination of sine and cosine.

***The sampling rate is better to set to be similar order to your frequenc(ies).***

## In-class Activity - Part III

Find the frequencies with real data!!!
1. Open ```FFT_DATA.txt``` and arbitrary choose TWO of the data sets.
2. Make the file excutable: 
```
chmod +x sin_activity.py
```
3. Run ```real_data_activity.py```
4. Compare your plot with different parameters (e.g. thresholds).

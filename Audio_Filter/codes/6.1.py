import numpy as np
import scipy.signal as signal
import soundfile as sf
import matplotlib.pyplot as plt

def custom_lfilter(b, a, x):
    def apply_filter(b, a, x):
        # Initialize the output array
        y = np.zeros_like(x)

        # Apply the filter
        for n in range(len(x)):
            for k in range(len(b)):
                if n - k >= 0:
                    y[n] += b[k] * x[n - k]
            for k in range(1, len(a)):
                if n - k >= 0:
                    y[n] -= a[k] * y[n - k]
        return y
    
    # Apply the custom filter along each column of x
    return np.apply_along_axis(lambda y: apply_filter(b, a, y), axis=0, arr=x)

# Load the input audio
x, fs = sf.read('inp.wav')

# Order of the filter
order = 3

# Cutoff frequency 4kHz
cutoff_freq = 5000.0  

# Digital frequency
Wn = 2 * cutoff_freq / fs 

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

# Filter the input signal with Butterworth filter using SciPy's lfilter
output_signal_scipy = signal.lfilter(b, a, x)

# Filter the input signal with Butterworth filter using custom lfilter
output_signal_custom = custom_lfilter(b, a, x)

output_signal_scipy_plot = [sublist[0] for sublist in output_signal_scipy]
output_signal_custom_plot = [sublist[0] for sublist in output_signal_custom]
# Plot

plt.plot(output_signal_scipy_plot, label='Scipy lfilter')
plt.plot(output_signal_custom_plot, label='Custom lfilter')
plt.legend()
plt.grid(True)
plt.savefig('lfilter.png')
plt.show()


import soundfile as sf
import numpy as np
from scipy import signal

#read .wav file 
input_signal,fs = sf.read('inp.wav') 

#order of the filter
order = 3

#cutoff frquency 
cutoff_freq = 5000.0  

#digital frequency
Wn=2*cutoff_freq/fs

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

output_signal = signal.lfilter(b, a, input_signal)

#write the output signal into .wav file
sf.write('Sound_With_ReducedNoise.wav', output_signal, fs) 

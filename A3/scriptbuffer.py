from scipy.fftpack import fft
import numpy as np
from fractions import gcd

"""
A3-Part-1: Minimize energy spread in DFT of sinusoids
Given a signal consisting of two sinusoids, write a function that selects the first M samples from 
the signal and returns the positive half of the DFT magnitude spectrum (in dB), such that it has 
only two non-zero values. 

M is to be calculated as the smallest positive integer for which the positive half of the DFT magnitude 
spectrum has only two non-zero values. To get the positive half of the spectrum, first compute the 
M point DFT of the input signal (for this you can use the fft function of scipy.fftpack, which is 
already imported in this script). Consider only the first (M/2)+1 samples of the DFT and compute the
magnitude spectrum of the positive half (in dB) as mX = 20*log10(abs(X[:M/2+1])), where X is the DFT 
of the input.

The input arguments to this function are the input signal x (of length W >= M) consisting of two 
sinusoids of frequency f1 and f2, the sampling frequency fs and the value of frequencies f1 and f2. 
The function should return the positive half of the magnitude spectrum mX. For this question, 
you can assume the input frequencies f1 and f2 to be positive integers and factors of fs, and 
that M is even. 

Due to the precision of the FFT computation, the zero values of the DFT are not zero but very small
values < 1e-12 (or -240 dB) in magnitude. For practical purposes, all values with absolute value less 
than 1e-6 (or -120 dB) can be considered to be zero. 

EXAMPLE: For an input x sampled at 10000 Hz and composed of sinusoids of frequency 80 Hz and 200 Hz, 
the DFT size for the required condition is M = 250 samples and the non-zero values in the DFT spectrum 
are at bin indices 2 and 5 (corresponding to the frequency values of 80 and 200 Hz, respectively). 
The output mX that the function returns is 126 samples in length. 


def minimizeEnergySpreadDFT(x, fs, f1, f2):
    """
    Inputs:
        x (numpy array) = input signal 
        fs (float) = sampling frequency in Hz
        f1 (float) = frequency of the first sinusoid component in Hz
        f2 (float) = frequency of the second sinusoid component in Hz
    Output:
        The function should return 
        mX (numpy array) = The positive half of the DFT spectrum of the M sample segment of x. 
                           mX is (M/2)+1 samples long (M is to be computed)
    """
    ## Your code here
    fs = f1 * f2/gcd(f1, f2)
    x= 0.8*np.cos(2*np.pi*

def genSine(A, f, phi, fs, t):
"""
import A3Part1 as a3p1

def gensineN(A, phi, f, N, fs):
    f = A * np.cos(2*np.pi*f*np.arange(N)/fs)
    return f

def createFFTBuffer( anArr ):
    sz=np.size(anArr)
    hM1 = int(math.floor((sz+1)/2))
    hM2 = int(math.floor(sz/2))
    fftBuffer=np.zeros(sz)
    fftBuffer[:hM1]=anArr[hM1:]
    fftBuffer[hM2:] = anArr[:hM2]
    return fftBuffer


fs=1000
f=100
W=15
x=a3p1.gensineN(1,0,f,W, fs)


def optimalZeropad(x, fs, f):
    """
    Inputs:
        x (numpy array) = input signal of length W
        fs (float) = sampling frequency in Hz
        f (float) = frequency of the sinusoid in Hz
    Output:
        The function should return
        mX (numpy array) = The positive half of the DFT spectrum of the M point DFT after zero-padding 
                        x appropriately (zero-padding length to be computed). mX is (M/2)+1 samples long
    """
    #create a sinusoidal signal
 
   

    X=fft(X)

    mX=20*np.log10(abs(X))

    cnt = np.size(mX[mX>-120])

    while cnt > 1 :
    
        x=np.append(x, 0) 

        X=fft(X)
        X=20*np.log10(abs(X))
        cnt = np.size(mX[mX>-120])
   return np.array(mX[:(np.size(mX)/2) + 1])



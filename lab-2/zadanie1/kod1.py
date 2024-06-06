import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft
from time import time

# Funkcje pomocnicze
def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N,1))
    e = np.exp(-2j*np.pi*k*n/N)
    X = np.dot(e,x)
    return X
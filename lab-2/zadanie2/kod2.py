import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft
from time import time

def oblicz_widmo_amplitudowe(X):
    Re_X = np.real(X)
    Im_X = np.imag(X)
    M = np.sqrt(Re_X**2+Im_X**2)  # widmo amplitudowe
    M_dB = 10*np.log10(M)  # widmo amplitudowe w skali decybelowej
    return M_dB

def oblicz_skale_czestotliwosci(fs, N):
    fk = np.arange(N//2)*fs/N
    return fk

def wyswietl_widmo_amplitudowe(M_dB, fk, title, filepath):
    plt.figure()
    plt.plot(fk, M_dB[:len(fk)])
    plt.title(title)
    plt.xlabel('Czestotliwosc [Hz]')
    plt.ylabel('Amplituda [dB]')
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True)
    plt.savefig(filepath)
    plt.close()
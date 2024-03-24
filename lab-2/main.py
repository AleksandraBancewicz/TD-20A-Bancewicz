'L02'
'Aleksandra Bancewicz'
'ba34753'

import matplotlib.pyplot as plt
import numpy as np

'Dyskretne przekształcenie Fouriera (DFT)'

'1. Wprowadzenie'

'X(k) - reprezentacja w dziedzinie czestotliwosci a +ib'
'x(n) - próbki reprezentujące sygnał w dziedznie czasu'
'i - jednostka urojona (i^^2 = -1)'
'N - iczba próbek sygnału w dziedzinie czasu i częstotliwości'

'tablica dla x(k) = x(n)[np.cos((2*np.pi*n*k)/N) - sin((2j*np.pi*n*k)/4)'
'complex number'
'r = x.real'
'i = x.imag'
'np.exp(-2j*np.pi*k*n/N)  ---- DOBRZE'

'A - amplituda'
'f - czestotliwosc'
'Y - faza'
'y = A* sin(s*np.pi*f*t+Y)'

'Ćwiczenia'

'Funckja z poprzednich laboratoriów:'
'////////////////////////////////////'
Tc = 1      #czas trwania sygnału - sekundy
fs = 8000       #częstotliwość próbkowania - Hz - 8kHz
N = Tc * fs     #liczba próbek przypadających na cały sygnał
Ts = 1/fs       #okres próbkowania
f = 4

tab = np.zeros(N)   #Inicjalizacja tablicy na sygnał
for n in range(N):
    t = n / fs  #czas odpowiadający próbce n
    'funkcja nr 12'
    x = np.sin(np.pi*(f/4)*t) + np.sin(1.4*np.pi*f*t) - np.cos(0.3*np.pi*f*t)
    tab[n] = x

czas = np.zeros(N)
for n in range(N):
    czas[n] = n / fs
'////////////////////////////////////////////'

'Zad 1'
'Implementacja DFT'

def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N,1))
    e = np.exp(-2j*np.pi*k*n/N)

    X = np.dot(e,x)

    return X

# Obliczenie DFT dla przykładowej funkcji
X = DFT(tab)
print(X)
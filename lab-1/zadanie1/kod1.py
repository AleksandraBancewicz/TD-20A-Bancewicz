import matplotlib.pyplot as plt
import numpy as np

'1.Wprowadzenie. Dane:'
Tc = 1      #czas trwania sygnału - sekundy
fs = 8000       #częstotliwość próbkowania - Hz - 8kHz
N = Tc * fs     #liczba próbek przypadających na cały sygnał
Ts = 1/fs       #okres próbkowania

a = 1       #amplituda

'2fmax <= fs'
'n=0,...,N-1'
't=n/fs=n*Ts'

'2.Ćwiczenia.'

'Zad.1'
f = 4      #częstotliwość sygnału próbkowanego
            # T=1/f  ->  f = 1/T

#'FUNKCJA CZASU (start, stop, krok):'
#t = np.arange(0,Tc,Ts)
#t = np.linspace(0,Tc, N)

#t=n/fs
#mamy tablice k wypełnioną próbkami i kazda probka ma dlugosc czasu
#a więc jednen przez fs, 2 przez fs itd.

#Dane:
tab = np.zeros(N)   #Inicjalizacja tablicy na sygnał
for n in range(N):
    t = n / fs  #czas odpowiadający próbce n
    'funkcja nr 12'
    x = np.sin(np.pi*(f/4)*t) + np.sin(1.4*np.pi*f*t) - np.cos(0.3*np.pi*f*t)
    tab[n] = x

czas = np.zeros(N)
for n in range(N):
    czas[n] = n / fs

plt.plot(czas, tab)
plt.title('Zad1 - funkcja nr 12')
plt.savefig('L1-Zad1-funkcja-nr-12')
plt.show()
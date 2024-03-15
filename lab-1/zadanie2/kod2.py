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

f = 4
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

'Zad.2'

'funkcje nr 2'
y = (tab*czas**3)/3
z = 1.92*(np.cos(3*np.pi*(czas/2))+np.cos(y**2/(8*tab+3)*czas))
v = ((y*z)/(tab+2))*np.cos(7.2*np.pi*czas)+np.sin(np.pi*czas**2)

plt.plot(czas, y)
plt.title('L1-Zad2-funkcje-nr-2-wykres1')
plt.savefig('L1-Zad2-funkcja-nr-12-wykres1')
plt.show()
plt.plot(czas, z)
plt.title('L1-Zad2-funkcje-nr-2-wykres2')
plt.savefig('L1-Zad2-funkcja-nr-12-wykres2')
plt.show()
plt.plot(czas, v)
plt.title('L1-Zad2-funkcje-nr-2-wykres3')
plt.savefig('L1-Zad2-funkcja-nr-12-wykres3')
plt.show()
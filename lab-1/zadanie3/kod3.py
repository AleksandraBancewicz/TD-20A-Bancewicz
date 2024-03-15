import matplotlib.pyplot as plt
import numpy as np

'1.Wprowadzenie. Dane:'
Tc = 1      #czas trwania sygnału - sekundy
fs = 8000       #częstotliwość próbkowania - Hz - 8kHz
N = Tc * fs     #liczba próbek przypadających na cały sygnał
Ts = 1/fs       #okres próbkowania

'Zad.3'
'funkcja nr 6'

#t1 = np.arange(0, 1.8, Ts/1.8)    #od 0 do 1.8
#u1 = (-1/2)*np.sin(20*t1**3-18*t1**2)

tu1 = 1.8 - 0
n1 = int(tu1 * fs)
t1 = np.zeros(n1)
u1 = np.zeros(n1)

for n in range(n1):
    t1[n] = n / fs
    u1[n] = (-1/2)*np.sin(20*t1[n]**3-18*t1[n]**2)

#t2 = np.arange(1.8, 3, Ts/1.2)    #od 1.8 do 3
#u2 = np.cos(5*np.pi*t2)*np.sin(12*np.pi*t2**2)

tu2 = 3 - 1.8
n2 = int(tu2 * fs)
t2 = np.zeros(n2)
u2 = np.zeros(n2)

for n in range(n2):
    t2[n] = n / fs + tu1
    u2[n] = np.cos(5*np.pi*t2[n])*np.sin(12*np.pi*t2[n]**2)

#t3 = np.arange(3, 4.5, Ts/1.5)   #od 3 do 4.5
#u3 = ((t3-3)/3)*np.sin((12-t3)*np.pi*t3**2)

tu3 = 4.5 - 3
n3 = int(tu3 * fs)
t3 = np.zeros(n3)
u3 = np.zeros(n3)

for n in range(n3):
    t3[n] = n / fs + tu1 + tu2
    u3[n] = np.cos(5*np.pi*t3[n])*np.sin(12*np.pi*t3[n]**2)

plt.plot(t1, u1)
plt.plot(t2, u2)
plt.plot(t3, u3)
plt.title('L1-Zad3-funkcje-nr-6-wykres')
plt.savefig('L1-Zad3-funkcja-nr-6-wykres')
plt.show()
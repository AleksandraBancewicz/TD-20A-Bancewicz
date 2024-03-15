import matplotlib.pyplot as plt
import numpy as np

'1.Wprowadzenie. Dane:'
Tc = 1      #czas trwania sygnału - sekundy
fs = 8000       #częstotliwość próbkowania - Hz - 8kHz
N = Tc * fs     #liczba próbek przypadających na cały sygnał
Ts = 1/fs       #okres próbkowania

'Zad.4'
'funkcja nr 1'
#bkt = np.arange(0, Tc, 1/22050)
    #dla Tc=1s oraz fs=22.05kHz=22050Hz,
    #wiec okres probkowania Ts 1/22050

fs4 = 22050

bkt = np.zeros(N)
for n in range(N):
    bkt[n] = n / fs4

bk1 = 0  #stan początkowy
h1 = 5
for i in range(1, h1+1):
    bk1 += (2*np.pi)*(((-1)**i)*np.sin(i*np.pi*2*bkt))

plt.plot(bkt, bk1)
plt.title('L1-Zad4-funkcja-nr-1-wykres1')
plt.savefig('L1-Zad4-funkcja-nr-1-wykres1')
plt.show()

bk2 = 0
h2 = 20
for i in range(1, h2+1):
    bk2 += (2*np.pi)*(((-1)**i)*np.sin(i*np.pi*2*bkt))

plt.plot(bkt, bk2)
plt.title('L1-Zad4-funkcja-nr-1-wykres2')
plt.savefig('L1-Zad4-funkcja-nr-1-wykres2')
plt.show()

bk3 = 0
h3 = 50
for i in range(1, h3+1):
    bk3 += (2*np.pi)*(((-1)**i)*np.sin(i*np.pi*2*bkt))

plt.plot(bkt, bk3)
plt.title('L1-Zad4-funkcja-nr-1-wykres3')
plt.savefig('L1-Zad4-funkcja-nr-1-wykres3')
plt.show()
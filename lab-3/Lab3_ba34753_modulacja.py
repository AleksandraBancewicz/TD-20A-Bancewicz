# BANCEWICZ ALEKSANDRA
# ba34753
# 21.04.2024

# Lab 3
# Modulacje amplitudy i kąta

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

# Zadanie 1 i 2

f = 4  # czestotliwosc 1/T
fi = 0  # faza sygnalu
fs = 200  # czestotliowsc probkowania (liczba probek w ciagu sekukndy)
Ts = 1/fs  # okres probkowania
Tc = 1  # czas czalkowity 1s
a = 1  # amplituda
N = Tc*fs  # liczba probek

t = np.arange(0, Tc, Ts)  # funkcja czasu start/stop/krok
# fn >> fm
fm = 4
fn = 50

# sygnał informacyjny
mt = np.sin(2*np.pi*fm*t)
plt.figure()
plt.plot(t, mt)
plt.title("Sygnał informacyjny")
plt.show()

########################################################

# sygnał zmodulowany amplitudowo
kaa = 0.5    # pkt.a
zaa = (kaa*mt+1)*np.cos(2*np.pi*fn*t)
plt.figure()
plt.plot(t, zaa)
plt.title("Modulacja amplitudy (ka=0.5)")
plt.show()

kab = 6    # pkt.b
zab = (kab*mt+1)*np.cos(2*np.pi*fn*t)
plt.figure()
plt.plot(t, zab)
plt.title("Modulacja amplitudy (ka=6)")
plt.show()

kac = 125   # pkt.c
zac = (kac*mt+1)*np.cos(2*np.pi*fn*t)
plt.figure()
plt.plot(t, zac)
plt.title("Modulacja amplitudy (ka=125)")
plt.show()

#######################################################

# sygnał zmodulowany kątowo - modulacja fazy
kpa = 0.25   # pkt.a
zpa = np.cos(2*np.pi*fn*t+kpa*mt)
plt.figure()
plt.plot(t, zpa)
plt.title("Modulacja fazowa (kp=0.25)")
plt.show()

kpb = 2.75  # pkt.b
zpb = np.cos(2*np.pi*fn*t+kpb*mt)
plt.figure()
plt.plot(t, zpb)
plt.title("Modulacja fazowa (kp=2.75)")
plt.show()

kpc = 3*np.pi   # pkt.c
zpc = np.cos(2*np.pi*fn*t+kpc*mt)
plt.figure()
plt.plot(t, zpc)
plt.title("Modulacja fazowa (kp=3*pi)")
plt.show()

############################################################

# sygnał zmodulowany kątowo - modulacja częstotliwości
kfa = 0.75   # pkt.a
zfa = np.cos(2*np.pi*fn*t+(kfa/fm)*mt)
plt.figure()
plt.plot(t, zfa)
plt.title("Modulacja częstotliwości (kf=0.75)")
plt.show()

kfb = 2.5   # pkt.b
zfb = np.cos(2*np.pi*fn*t+(kfb/fm)*mt)
plt.figure()
plt.plot(t, zfb)
plt.title("Modulacja częstotliwości (kf=2.5)")
plt.show()

kfc = 3*np.pi   # pkt.c
zfc = np.cos(2*np.pi*fn*t+(kfc/fm)*mt)
plt.figure()
plt.plot(t, zfc)
plt.title("Modulacja częstotliwości (kf=3*pi)")
plt.show()

######################################################

# Zadanie 3
# Widmo amplitudowe - transformata Fouriera

widmo_amp1 = np.fft.fft(zaa)
plt.plot(widmo_amp1)
plt.xlabel('czestotliwosc [Hz]')
plt.ylabel('amplituda widma')
plt.title('Widmo sygnału zaa')
plt.show()

widmo_amp2 = np.fft.fft(zab)
plt.plot(widmo_amp2)
plt.xlabel('czestotliwosc [Hz]')
plt.ylabel('amplituda widma')
plt.title('Widmo sygnału zab')
plt.show()

widmo_amp3 = np.fft.fft(zac)
plt.plot(widmo_amp3)
plt.xlabel('czestotliwosc [Hz]')
plt.ylabel('amplituda widma')
plt.title('Widmo sygnału zac')
plt.show()

########################################

widmo_amp4 = np.fft.fft(zpa)
plt.plot(widmo_amp4)
plt.xlabel('czestotliwosc [Hz]')
plt.ylabel('amplituda widma')
plt.title('Widmo sygnału zpa')
plt.show()

widmo_amp5 = np.fft.fft(zpb)
plt.plot(widmo_amp5)
plt.xlabel('czestotliwosc [Hz]')
plt.ylabel('amplituda widma')
plt.title('Widmo sygnału zpb')
plt.show()

widmo_amp6 = np.fft.fft(zpc)
plt.plot(widmo_amp6)
plt.xlabel('czestotliwosc [Hz]')
plt.ylabel('amplituda widma')
plt.title('Widmo sygnału zpc')
plt.show()

########################################

widmo_amp7 = np.fft.fft(zfa)
plt.plot(widmo_amp7)
plt.xlabel('czestotliwosc [Hz]')
plt.ylabel('amplituda widma')
plt.title('Widmo sygnału zfa')
plt.show()

widmo_amp8 = np.fft.fft(zfb)
plt.plot(widmo_amp8)
plt.xlabel('czestotliwosc [Hz]')
plt.ylabel('amplituda widma')
plt.title('Widmo sygnału zfb')
plt.show()

widmo_amp9 = np.fft.fft(zfc)
plt.plot(widmo_amp9)
plt.xlabel('czestotliwosc [Hz]')
plt.ylabel('amplituda widma')
plt.title('Widmo sygnału zfc')
plt.show()

# Zadanie 4
# SZEROKOSC PASMA

# zrobic dla widma
# B3dB, B6dB, B12dB


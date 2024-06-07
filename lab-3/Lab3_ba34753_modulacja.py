# BANCEWICZ ALEKSANDRA
# ba34753
# 21.04.2024

# Lab 3
# Modulacje amplitudy i kąta

import numpy as np
import matplotlib.pyplot as plt

# Zadanie 1 i 2

f = 4  # czestotliwosc 1/T
fi = 0  # faza sygnalu
fs = 200  # czestotliowsc probkowania (liczba probek w ciagu sekukndy)
Ts = 1/fs  # okres probkowania
Tc = 1  # czas calkowity 1s
a = 1  # amplituda
N = Tc * fs  # liczba probek

t = np.arange(0, Tc, Ts)  # funkcja czasu start/stop/krok
# fn >> fm
fm = 4
fn = 50

# sygnał informacyjny
mt = np.sin(2 * np.pi * fm * t)
plt.figure()
plt.plot(t, mt)
plt.title("Sygnał informacyjny")
plt.savefig('sygnal_informacyjny.png')
plt.show()

########################################################

# sygnał zmodulowany amplitudowo
kaa = 0.5  # pkt.a
zaa = (kaa * mt + 1) * np.cos(2 * np.pi * fn * t)
plt.figure()
plt.plot(t, zaa)
plt.title("Modulacja amplitudy (ka=0.5)")
plt.savefig('modulacja_amplitudy_ka_0.5.png')
plt.show()

kab = 6  # pkt.b
zab = (kab * mt + 1) * np.cos(2 * np.pi * fn * t)
plt.figure()
plt.plot(t, zab)
plt.title("Modulacja amplitudy (ka=6)")
plt.savefig('modulacja_amplitudy_ka_6.png')
plt.show()

kac = 125  # pkt.c
zac = (kac * mt + 1) * np.cos(2 * np.pi * fn * t)
plt.figure()
plt.plot(t, zac)
plt.title("Modulacja amplitudy (ka=125)")
plt.savefig('modulacja_amplitudy_ka_125.png')
plt.show()

#######################################################

# sygnał zmodulowany kątowo - modulacja fazy
kpa = 0.25  # pkt.a
zpa = np.cos(2 * np.pi * fn * t + kpa * mt)
plt.figure()
plt.plot(t, zpa)
plt.title("Modulacja fazowa (kp=0.25)")
plt.show()

kpb = 2.75  # pkt.b
zpb = np.cos(2 * np.pi * fn * t + kpb * mt)
plt.figure()
plt.plot(t, zpb)
plt.title("Modulacja fazowa (kp=2.75)")
plt.savefig('modulacja_fazowa_kp_2.75.png')
plt.show()

kpc = 3 * np.pi  # pkt.c
zpc = np.cos(2 * np.pi * fn * t + kpc * mt)
plt.figure()
plt.plot(t, zpc)
plt.title("Modulacja fazowa (kp=3*pi)")
plt.savefig('modulacja_fazowa_kp_3pi.png')
plt.show()

############################################################

# sygnał zmodulowany kątowo - modulacja częstotliwości
kfa = 0.75  # pkt.a
zfa = np.cos(2 * np.pi * fn * t + (kfa / fm) * mt)
plt.figure()
plt.plot(t, zfa)
plt.title("Modulacja częstotliwości (kf=0.75)")
plt.savefig('modulacja_czestotliwosci_kf_0.75.png')
plt.show()

kfb = 2.5  # pkt.b
zfb = np.cos(2 * np.pi * fn * t + (kfb / fm) * mt)
plt.figure()
plt.plot(t, zfb)
plt.title("Modulacja częstotliwości (kf=2.5)")
plt.savefig('modulacja_czestotliwosci_kf_2.5.png')
plt.show()

kfc = 3 * np.pi  # pkt.c
zfc = np.cos(2 * np.pi * fn * t + (kfc / fm) * mt)
plt.figure()
plt.plot(t, zfc)
plt.title("Modulacja częstotliwości (kf=3*pi)")
plt.savefig('modulacja_czestotliwosci_kf_3pi.png')
plt.show()

######################################################

# Zadanie 3
# Widmo amplitudowe - transformata Fouriera

def plot_spectrum(signal, fs, title):
    spectrum = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1/fs)
    plt.figure()
    plt.plot(freqs[:len(freqs)//2], np.abs(spectrum[:len(spectrum)//2]))
    plt.xlabel('Częstotliwość [Hz]')
    plt.ylabel('Amplituda widma')
    plt.title(title)
    plt.savefig(title)
    plt.show()
    return spectrum

widmo_amp1 = plot_spectrum(zaa, fs, 'Widmo sygnału zaa')
widmo_amp2 = plot_spectrum(zab, fs, 'Widmo sygnału zab')
widmo_amp3 = plot_spectrum(zac, fs, 'Widmo sygnału zac')
widmo_amp4 = plot_spectrum(zpa, fs, 'Widmo sygnału zpa')
widmo_amp5 = plot_spectrum(zpb, fs, 'Widmo sygnału zpb')
widmo_amp6 = plot_spectrum(zpc, fs, 'Widmo sygnału zpc')
widmo_amp7 = plot_spectrum(zfa, fs, 'Widmo sygnału zfa')
widmo_amp8 = plot_spectrum(zfb, fs, 'Widmo sygnału zfb')
widmo_amp9 = plot_spectrum(zfc, fs, 'Widmo sygnału zfc')

# Zadanie 4

def szerokosc_pasma(spectrum, fs, dB_poziom):
    amplituda = np.abs(spectrum)
    max_amplituda = np.max(amplituda)
    poziom_amplituda = max_amplituda * (10**(dB_poziom / 20))

    # Znajdowanie indeksów, w których amplituda jest powyżej poziomu dB
    powyzej_dB = np.where(amplituda > poziom_amplituda)[0]
    if len(powyzej_dB) == 0:
        return 0

    f_min = powyzej_dB[0]
    f_max = powyzej_dB[-1]

    pasmo = (f_max - f_min) * (fs / len(spectrum))
    return pasmo

# Obliczanie szerokości pasma dla każdego sygnału
B3dB1 = szerokosc_pasma(widmo_amp1, fs, -3)
B6dB1 = szerokosc_pasma(widmo_amp1, fs, -6)
B12dB1 = szerokosc_pasma(widmo_amp1, fs, -12)

print("Szerokość pasma dla zaa: B3dB =", B3dB1, "Hz, B6dB =", B6dB1, "Hz, B12dB =", B12dB1, "Hz")

B3dB2 = szerokosc_pasma(widmo_amp2, fs, -3)
B6dB2 = szerokosc_pasma(widmo_amp2, fs, -6)
B12dB2 = szerokosc_pasma(widmo_amp2, fs, -12)

print("Szerokość pasma dla zab: B3dB =", B3dB2, "Hz, B6dB =", B6dB2, "Hz, B12dB =", B12dB2, "Hz")

B3dB3 = szerokosc_pasma(widmo_amp3, fs, -3)
B6dB3 = szerokosc_pasma(widmo_amp3, fs, -6)
B12dB3 = szerokosc_pasma(widmo_amp3, fs, -12)

print("Szerokość pasma dla zac: B3dB =", B3dB3, "Hz, B6dB =", B6dB3, "Hz, B12dB =", B12dB3, "Hz")

B3dB4 = szerokosc_pasma(widmo_amp4, fs, -3)
B6dB4 = szerokosc_pasma(widmo_amp4, fs, -6)
B12dB4 = szerokosc_pasma(widmo_amp4, fs, -12)

print("Szerokość pasma dla zpa: B3dB =", B3dB4, "Hz, B6dB =", B6dB4, "Hz, B12dB =", B12dB4, "Hz")

B3dB5 = szerokosc_pasma(widmo_amp5, fs, -3)
B6dB5 = szerokosc_pasma(widmo_amp5, fs, -6)
B12dB5 = szerokosc_pasma(widmo_amp5, fs, -12)

print("Szerokość pasma dla zpb: B3dB =", B3dB5, "Hz, B6dB =", B6dB5, "Hz, B12dB =", B12dB5, "Hz")

B3dB6 = szerokosc_pasma(widmo_amp6, fs, -3)
B6dB6 = szerokosc_pasma(widmo_amp6, fs, -6)
B12dB6 = szerokosc_pasma(widmo_amp6, fs, -12)

print("Szerokość pasma dla zpc: B3dB =", B3dB6, "Hz, B6dB =", B6dB6, "Hz, B12dB =", B12dB6, "Hz")

B3dB7 = szerokosc_pasma(widmo_amp7, fs, -3)
B6dB7 = szerokosc_pasma(widmo_amp7, fs, -6)
B12dB7 = szerokosc_pasma(widmo_amp7, fs, -12)

print("Szerokość pasma dla zfa: B3dB =", B3dB7, "Hz, B6dB =", B6dB7, "Hz, B12dB =", B12dB7, "Hz")

B3dB8 = szerokosc_pasma(widmo_amp8, fs, -3)
B6dB8 = szerokosc_pasma(widmo_amp8, fs, -6)
B12dB8 = szerokosc_pasma(widmo_amp8, fs, -12)

print("Szerokość pasma dla zfb: B3dB =", B3dB8, "Hz, B6dB =", B6dB8, "Hz, B12dB =", B12dB8, "Hz")

B3dB9 = szerokosc_pasma(widmo_amp9, fs, -3)
B6dB9 = szerokosc_pasma(widmo_amp9, fs, -6)
B12dB9 = szerokosc_pasma(widmo_amp9, fs, -12)

print("Szerokość pasma dla zfc: B3dB =", B3dB9, "Hz, B6dB =", B6dB9, "Hz, B12dB =", B12dB9, "Hz")
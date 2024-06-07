'L04'
'Bancewicz Aleksandra'
'ba34753'

'Kluczowanie częstotliwości, amplitudy i fazy (I)'

import numpy as np
import matplotlib.pyplot as plt

def text_to_bitstream(text):
    """
    Funkcja zamieniająca dowolny napis w formacie ASCII (kody od 32 do 127)
    na strumień bitowy, gdzie każdemu znakowi odpowiada 7-bitowa reprezentacja binarna.

    Parametry:
    - text (str): Napis wejściowy.

    Zwraca:
    - bitstream (list): Lista zawierająca strumień bitowy.
    """
    bitstream = []
    for char in text:
        # Konwersja znaku na kod ASCII (liczba całkowita)
        ascii_code = ord(char)
        # Konwersja kodu ASCII na 7-bitowy strumień binarny (bez prefiksu '0b')
        binary_code = format(ascii_code, '07b')
        # Dodanie każdego bitu do strumienia bitowego
        bitstream.extend([int(bit) for bit in binary_code])
    return bitstream

def generate_signals(bitstream, Tb, A1, A2, W):
    """
    Funkcja generująca sygnały zmodulowane dla kluczowania amplitudy (ASK),
    fazy (PSK) i częstotliwości (FSK), oraz ich wykresy czasowe.

    Parametry:
    - bitstream (list): Strumień bitowy.
    - Tb (float): Czas trwania pojedynczego bitu [s].
    - A1 (float): Amplituda dla bitu 0.
    - A2 (float): Amplituda dla bitu 1.
    - W (int): Parametr dla częstotliwości nośnej.

    Zwraca:
      - zat, zpt, zft (np.ndarray): Sygnały zmodulowane.
    """
    # Liczba bitów sygnału informacyjnego
    B = len(bitstream)

    # Czas trwania całego sygnału
    Tc = Tb * B

    # Częstotliwość nośna
    fn = W / Tb
    fn1 = (W + 1) / Tb
    fn2 = (W + 2) / Tb

    # Generowanie czasu próbkowania
    fs = 2 * fn  # Spełnienie warunku próbkowania
    t = np.linspace(0, Tc, int(fs * Tc))

    # Inicjalizacja sygnałów zmodulowanych
    zat = np.zeros_like(t)
    zpt = np.zeros_like(t)
    zft = np.zeros_like(t)

    # Generowanie sygnałów zmodulowanych
    for i, bit in enumerate(bitstream):
        # Kluczowanie z przesuwem amplitudy (ASK)
        zat[i * int(fs * Tb): (i + 1) * int(fs * Tb)] = A1 if bit == 0 else A2
        # Kluczowanie z przesuwem fazy (PSK)
        zpt[i * int(fs * Tb): (i + 1) * int(fs * Tb)] = np.sin(2 * np.pi * fn * t[i * int(fs * Tb): (i + 1) * int(fs * Tb)]) if bit == 0 else np.sin(2 * np.pi * fn * t[i * int(fs * Tb): (i + 1) * int(fs * Tb)] + np.pi)
        # Kluczowanie z przesuwem częstotliwości (FSK)
        zft[i * int(fs * Tb): (i + 1) * int(fs * Tb)] = np.sin(2 * np.pi * fn1 * t[i * int(fs * Tb): (i + 1) * int(fs * Tb)]) if bit == 0 else np.sin(2 * np.pi * fn2 * t[i * int(fs * Tb): (i + 1) * int(fs * Tb)])

    # Wygenerowanie wykresów czasowych
    plt.figure()
    plt.plot(t, zat)
    plt.title('Sygnał zmodulowany ASK')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.savefig('zmodulowany_ASK.jpg')
    plt.show()

    plt.figure()
    plt.plot(t, zpt)
    plt.title('Sygnał zmodulowany PSK')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.savefig('zmodulowany_PSK.jpg')
    plt.show()

    plt.figure()
    plt.plot(t, zft)
    plt.title('Sygnał zmodulowany FSK')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.savefig('zmodulowany_FSK.jpg')
    plt.show()

    return zat, zpt, zft

def plot_spectrum(signal, fs, title):
    """
    Funkcja generująca widmo amplitudowe w skali decybelowej dla danego sygnału.

    Parametry:
    - signal (np.ndarray): Sygnał zmodulowany.
    - fs (float): Częstotliwość próbkowania.
    - title (str): Tytuł wykresu.

    Zwraca:
    - None
    """
    N = len(signal)
    f = np.fft.fftfreq(N, 1/fs)
    spectrum = np.fft.fft(signal)
    spectrum_amplitude = 20 * np.log10(np.abs(spectrum))

    plt.figure()
    plt.plot(f[:N//2], spectrum_amplitude[:N//2])
    plt.title(title)
    plt.xlabel('Częstotliwość [Hz]')
    plt.ylabel('Amplituda [dB]')
    plt.savefig(title)
    plt.show()

    return f, spectrum_amplitude

def szerokosc_pasma(spectrum_amplitude, fs, dB_poziom):
    amplituda = np.abs(spectrum_amplitude)
    max_amplituda = np.max(amplituda)
    poziom_amplituda = max_amplituda * (10**(dB_poziom/20))

    ponizej_dB = np.where(amplituda > poziom_amplituda)[0]
    if len(ponizej_dB) == 0:
        return 0
    f_min = ponizej_dB[0]
    f_max = ponizej_dB[-1]

    pasmo = (f_max - f_min) * (fs / len(spectrum_amplitude))
    return pasmo

# Przykładowy tekst
tekst = "abcd"
# Zamiana tekstu na strumień bitowy
bitstream = text_to_bitstream(tekst)

# Parametry modulacji
Tb = 1          # Czas trwania pojedynczego bitu [s]
A1 = 1.0        # Amplituda dla bitu 0
A2 = 2.0        # Amplituda dla bitu 1
W = 2           # Parametr dla częstotliwości nośnej

# Generowanie sygnałów zmodulowanych i ich wykresów czasowych
zat, zpt, zft = generate_signals(bitstream, Tb, A1, A2, W)

# Częstotliwość próbkowania
fs = 2 * (W / Tb)

f_zat, spectrum_amplitude_zat = plot_spectrum(zat, fs, 'Widmo amplitudowe sygnału zmodulowanego ASK')
f_zpt, spectrum_amplitude_zpt = plot_spectrum(zpt, fs, 'Widmo amplitudowe sygnału zmodulowanego PSK')
f_zft, spectrum_amplitude_zft = plot_spectrum(zft, fs, 'Widmo amplitudowe sygnału zmodulowanego FSK')

B3dB_ASK = szerokosc_pasma(spectrum_amplitude_zat, fs, -3)
B6dB_ASK = szerokosc_pasma(spectrum_amplitude_zat, fs, -6)
B12dB_ASK = szerokosc_pasma(spectrum_amplitude_zat, fs, -12)

B3dB_PSK = szerokosc_pasma(spectrum_amplitude_zpt, fs, -3)
B6dB_PSK = szerokosc_pasma(spectrum_amplitude_zpt, fs, -6)
B12dB_PSK = szerokosc_pasma(spectrum_amplitude_zpt, fs, -12)

B3dB_FSK = szerokosc_pasma(spectrum_amplitude_zft, fs, -3)
B6dB_FSK = szerokosc_pasma(spectrum_amplitude_zft, fs, -6)
B12dB_FSK = szerokosc_pasma(spectrum_amplitude_zft, fs, -12)

print("Szerokość pasma dla ASK: B3dB =", B3dB_ASK, "Hz, B6dB =", B6dB_ASK, "Hz, B12dB =", B12dB_ASK, "Hz")
print("Szerokość pasma dla PSK: B3dB =", B3dB_PSK, "Hz, B6dB =", B6dB_PSK, "Hz, B12dB =", B12dB_PSK, "Hz")
print("Szerokość pasma dla FSK: B3dB =", B3dB_FSK, "Hz, B6dB =", B6dB_FSK, "Hz, B12dB =", B12dB_FSK, "Hz")
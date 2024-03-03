'L01'
'Aleksandra Bancewicz'
'ba34753'

import matplotlib.pyplot as plt
import numpy as np

'dane:'
x = np.arange(0, 2*np.pi, 0.1)

'obliczenie wartosci funkcji:'
y=np.sin(x)

'Tworzenie wykresu'
plt.plot(x,y)
plt.title('Wykres funkcji sinus')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.savefig('wykres0.png')
plt.show()

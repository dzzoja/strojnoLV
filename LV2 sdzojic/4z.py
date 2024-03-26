import numpy as np  # Uvoz numpy biblioteke i postavljanje np za kasnije koristnje
import matplotlib.pyplot as plt  # Uvoz modula pyplot iz matplotlib biblioteke

# Definicija funkcije check() koja generira šahovsku ploču s crnim i bijelim kvadratima
def crtanje(kvadrat, redovi, stupci):
    # Stvaranje crne kvadratne matrice
    crne = np.zeros((kvadrat, kvadrat))
    # Stvaranje bijele kvadratne matrice postavljanje svih elemenata na 255 (bijela boja)
    bijele = np.ones((kvadrat, kvadrat)) * 255
    
    # Stvaranje prvog retka šahovske ploče
    red1 = np.hstack([crne, bijele] * (stupci // 2))  # Spajanje crnih i bijelih kvadrata u redak
    if stupci % 2 != 0:  # Ako je broj stupaca neparan, dodajemo crni na kraj retka
        red1 = np.hstack([red1, crne])
    
    # Stvaranje drugog retka šahovske ploče
    red2 = np.hstack([bijele, crne] * (stupci // 2))  # Spajanje bijelih i crnih kvadrata u redak
    if stupci % 2 != 0:  # Ako je broj stupaca neparan, dodajemo bijeli na kraj retka
        red2 = np.hstack([red2, bijele])

    polje = np.vstack([red1, red2] * (redovi // 2))  # Ponavljanje redaka red1 i red2, ovisno o broju redova
    if redovi % 2 != 0:  # Ako je broj redova neparan, dodajemo red1 na kraj
        polje = np.vstack([polje, red1])
    return polje  # Vraća generiranu šahovsku ploču

# Generiranje šahovske
img = crtanje(100, 8, 8)

# Prikazivanje šahovske ploče na grafikonu koristeći imshow()
plt.imshow(img, cmap='gray', vmin=0, vmax=255)  # Postavljanje parametara za prikaz slike u sivoj skali
plt.show()  # Prikaz korisniku

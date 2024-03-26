from matplotlib import pyplot as plt
import numpy as np

# Učitavanje slike "tiger.png" u niz img
img = plt.imread("tiger.png")
# Kopiranje samo crvenog kanala slike u novi niz img
img = img[:,:,0].copy()

# Inicijalizacija prazne liste img_array
img_array=[]

# Dodavanje konstante 0.6 svakom pikselu u slici kako bi se povećala svjetlina slike
img_array=img+0.6
# Postavljanje svih vrijednosti većih od 1 na 1 u nizu img_array
img_array[img_array>1]=1

img1 = np.rot90(img,3) # Rotacija slike
img2 = np.fliplr(img) # horizontalno zrcaljenje
img3 = img[::5,::5] # zadrzavamo svaki 5. piksel u stupcima/retcima

# Određivanje broja redova i stupaca slike
redovi = img.shape[0]
stupci = img.shape[1]
# Određivanje granica za odsijecanje dijelova slike, od cetvrtine do polovine
dg = stupci//4
gg = stupci//2

# Kopiranje slike u novu sliku pr_img
pr_img = img.copy()
# sve piksele van dg/gg stavljamo na 0
for i in range(redovi):
    for j in range(stupci):
        if (j < dg or j > gg): 
            pr_img[i][j] = 0

# Crtanje slika s imshow() i figure()
plt.figure(1)
plt.title("a) brightness")
plt.imshow(img_array,cmap='gray')

plt.figure(2)
plt.title("b) rotirana slika")
plt.imshow(img1,cmap='gray')

plt.figure(3)
plt.title("c) zrcaljena slika")
plt.imshow(img2,cmap='gray')

plt.figure(4)
plt.title("d) smanjena kvaliteta slike")
plt.imshow(img3,cmap='gray')

plt.figure(5)
plt.title("e) stupci")
plt.imshow(pr_img, cmap='gray')

# prikaz slika korisniku
plt.show()

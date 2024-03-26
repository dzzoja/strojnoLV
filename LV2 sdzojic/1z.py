import numpy as np  # uvoz biblioteke numpy i omogućava korištenje nizova i matrica
import matplotlib.pyplot as plt  # uvoz podmodula pyplot iz biblioteke matplotlib, koji omogućava crtanje grafova

x = np.array([1, 2, 3, 3, 1])  
y = np.array([1, 2, 2, 1, 1])  #postavljanje tocaka x i y

plt.plot(x, y, 'b-', linewidth=2, markersize=5, marker='o') 
# Crtanje grafa s xy, plavom punom linijom, postavljanje debljine i stavljanje tocki na vrhove
plt.axis([0, 4, 0, 4])  # postavljanje granica za x i y
plt.xlabel('x os') 
plt.ylabel('y os')  # postavljanje oznaka za x/y osi
plt.title('Primjer')  # title za postavljanje naslova
plt.show()  #prikaz grafa korisniku

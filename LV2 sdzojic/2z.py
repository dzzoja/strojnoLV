import numpy as np  # uvoz biblioteke numpy i omogućava korištenje nizova i matrica
import matplotlib.pyplot as plt  # uvoz podmodula pyplot iz biblioteke matplotlib, koji omogućava crtanje grafova

# Učitavanje podataka iz datoteke
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

plt.ylabel('snaga(hs)') 
plt.xlabel('potrošnja')  
plt.title('Potrosnja automobila')  

# Ispis min max i average potrosnje auta
print("min mpg: ", min(data[:, 0]))
print("max mpg: ", max(data[:, 0]))
print("avg mpg: ", sum(data[:, 0])/len(data[:, 0]))

# filtriramo podatke samo za aute s 6 cilindara
arr = data[:, 1] == 6

#data 0,3 za uzimanje mpg i hp, c za boju, ec za boju ruba,s=data za velicinu proporcionalnu tezini auta
plt.scatter(data[:, 0], data[:, 3], c='red', ec='k', s=data[:, 5]*16, marker="o")

# ispis tezine pored točkica za auta
for i, label in enumerate(data[:, 5]):
    plt.text(data[i, 0], data[i, 3]+5, str(data[i, 5]))

# ispis min max i average potrosnje auta s 6 cilindara
print("min mpg sa 6 cyl: ", min(data[arr, 0]))
print("max mpg sa 6 cyl: ", max(data[arr, 0]))
print("avg mpg sa 6 cyl: ", sum(data[arr, 0])/len(data[arr, 0]))

# prikaz grafa
plt.show()

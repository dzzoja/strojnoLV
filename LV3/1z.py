import pandas as pd              # Pandas biblioteka za manipulaciju podacima
import numpy as np               # NumPy biblioteka za numeričke operacije
import matplotlib.pyplot as plt  # Matplotlib za crtanje grafova

# Učitavanje podataka iz 'mtcars.csv' u DataFrame 'mtcars'
mtcars = pd.read_csv('mtcars.csv')

# 1.1. Ispis pet automobila s najvećom potrošnjom goriva (mpg)
print("\nPet automobila s najvećom potrošnjom\n", mtcars.sort_values(by=['mpg']).tail(5))

# 1.2. Filtriranje automobila s osam cilindara i ispis tri automobila s najmanjom potrošnjom goriva među njima
osam_cilindara = mtcars[mtcars.cyl == 8]
print("\nTri automobila s 8 cil i najmanjom potrosnjom\n", osam_cilindara.sort_values(by=['mpg']).head(3))

# 1.3. Izračun i ispis prosječne potrošnje goriva automobila s šest cilindara
sest_cilindara = mtcars[mtcars.cyl == 6]
print("\nSrednja potrosnja automobila sa 6 cil: ", sest_cilindara['mpg'].mean())

# 1.4. Izračun i ispis prosječne potrošnje goriva automobila s četiri cilindra i masom između 2000 i 2200 lbs
cetri_cilindra_masa2000 = mtcars[(mtcars.cyl == 4) & ((mtcars.wt >= 2) & (mtcars.wt <= 2.2))]
print("\nSrednja potrosnja automobila s 4 cil i masom između 2000 i 2200: ", cetri_cilindra_masa2000['mpg'].mean())

# 1.5. Brojanje automobila s ručnim i automatskim mjenjačem
broj_automatski = mtcars[mtcars['am'] == 1]['am'].count()
broj_rucni = mtcars[mtcars['am'] == 0]['am'].count()

print("\nBroj automobila s automatskim mjenjačem:", broj_automatski)
print("Broj automobila s ručnim mjenjačem:", broj_rucni)

# 1.6. Brojanje automobila s automatskim mjenjačem i više od 100 konjskih snaga
am_hp100 = mtcars[(mtcars.am == 1) & (mtcars.hp > 100)]
print("\nBroj automobila s automatskim mj. i više od 100hp: ", len(am_hp100))

# 1.7. Pretvaranje mase svih automobila iz lbs u kilograme i ispis
masa = round(mtcars.wt * 1000 / 0.45359237, 2)
print("\nMase svih automobila u KG")
print(masa)

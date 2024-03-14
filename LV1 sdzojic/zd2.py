try:
    broj = float(input("Unesite ocjenu[0.0, 1.0]: ")) 
except:
    print("Pogresan unos")  #ako nije broj ispisuje gresku

if (broj > 1 or broj < 0):  #ako je van intervala ispisuje gresku
    print("Broj nije u zadanom intervalu")
elif (broj >= 0.9):  
    print("A")
elif (broj >= 0.8):  
    print("B")
elif (broj >= 0.7):
    print("C")
elif (broj >= 0.6): 
    print("D")
else:
    print("F")

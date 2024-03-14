lst = []
lstCheck = 0
suma = 0

while lstCheck == 0:
    broj = input("Unesite broj ili 'Done' za kraj: ")
    if broj.isdigit() or broj == "Done":
        lst.append(broj)
        if broj.isdigit():
            suma += int(broj)
    else:
        print("Molim unesite broj") 

    lstCheck = lst.count("Done") #check Done+1

lst.pop(-1)

lst = [float(x) for x in lst] #konvertiranje svih elemenata u brojeve

if len(lst) < 1:
    print("Nema unesenih brojeva")  #ako je lista prazna
    exit()
print("Lista: ", sorted(lst))  #sorted za sortiranje liste
print("Najveci broj: ", max(lst))  #max za najveci broj
print("Najmanji broj: ", min(lst))  #min za najmanji broj liste
print("Uneseno brojeva: ", len(lst))  #len za duzinu niza
print("Prosjecna vrijednost unesenih brojeva: ", suma/len(lst))  #prosjek

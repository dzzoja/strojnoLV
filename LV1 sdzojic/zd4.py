ime_datoteke = input("Ime datoteke: ") 
dat_dir = "C:\\Users\\student\\Desktop\\LV1 sdzojic\\" + ime_datoteke  #putanja do datoteke

try:
    datoteka = open(dat_dir, 'r')  #otvaranje datoteke, r = za citanje
except:
    print("Datoteka ne postoji!")  #ako nije pronadjen file ispis poruke

suma = 0 
brojac = 0  

for line in datoteka:  #prolazak kroz linije
    line = line.rsplit()  #rsplit razdvaja liniju na riječi
    if "X-DSPAM-Confidence:" in line:  # provjera za "X-DSPAM-Confidence:"
        brojac += 1
        suma += float(line[1])  #dodavanje vrijednost X-DSPAMA na sumu

print("Average X-DSPAM-Confidence: ", suma/brojac)  #prosjek

datoteka.close()


dat = open("C:\\Users\\student\\Desktop\\LV1 sdzojic\\song.txt", 'r') # Otvaranje datoteke "song.txt" za čitanje

rijecnik = {} #postavljanje praznog rjecnika

#prolazak kroz linije
for line in dat:
    line = line.rsplit() #rsplit za razdvajanje na riječi
    for rijec in line:
        #update riječnika
        if rijec in rijecnik:
            rijecnik[rijec] += 1
        else:
            rijecnik[rijec] = 1

#singular rijeci u rijecniku
jedinstvene_rijeci = []

#provjera jedinstvenih rijeci
for rijec in rijecnik:
    if rijecnik[rijec] == 1: 
        jedinstvene_rijeci.append(rijec)   # ako rijec == 1 dodaje se na listu jedinstvenih

#print(rijecnik) # cijeli riječnik

print("Broj unikatnih rijeci: ", len(jedinstvene_rijeci)) # ukupno jedinstvenih rijeci

print(jedinstvene_rijeci) #ispis jedinstvenih riječi

dat.close()

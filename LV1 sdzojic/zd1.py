def total_euro(radni_sati, eur_h):
    print("Ukupno: ", radni_sati * eur_h) #def funkcije i ispis zarade

radni_sati = int(input("Radni sati: "))
eur_h = float(input("Satnica(€/h): ")) 

total_euro(radni_sati, eur_h) #poziv funkcije

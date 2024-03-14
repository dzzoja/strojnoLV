dat = open("C:\\Users\\student\\Desktop\\LV1 sdzojic\\SMSSpamCollection.txt", 'r') #otvori file za citanje

brojac_ham = 0
brojac_spam = 0
rijeci_ham = 0
rijeci_spam = 0
brojac_usklicnik = 0

#prolazak kroz linije
for line in dat:
    line = line.rsplit()
    if line[0] == "ham":
        brojac_ham += 1
        rijeci_ham += len(line) #dodavanje u ham brojac
    if line[0] == "spam":
        brojac_spam += 1
        rijeci_spam += len(line) #dodavanje u spam brojac
        if "!" in line[-1]:
            brojac_usklicnik += 1 #brojanje spam poruka s usklicnikom


print("Prosjecan broj rijeci u ham porukama: ", rijeci_ham / brojac_ham)
print("Prosjecan broj rijeci u spam porukama: ", rijeci_spam / brojac_spam)
print("Broj poruka koje su spam i zavrsavaju s usklicnikom: ", brojac_usklicnik)

dat.close()

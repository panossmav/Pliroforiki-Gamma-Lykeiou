payment = 5000 #Δόση
total = 0 #Σύνολο
i = 0

while total <=600000:
    total+=payment
    payment*=2
    i+=1
print('Χρειάζονται ',i,' εβδομάδες.')
if total > 600000:
    print('Υπολέίπονται ',total-600000,'δρχ.')
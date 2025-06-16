def calc_cost(time): #Συνάρτηση υπολογισμού κόστους 
    if time <=3:
        cost = time*2
    elif time <=5:
        cost = (3*2)+((time-3)*1.5)
    else:
        cost = (3*2)+(2*1.5)+((time-5)*1.3)
    return cost

plate = 'None' #Αρ. Κυκλοφορίας

o_2h = 0 #Πλήθος οχημάτων παραμονής > 2 ωρών.

while True: #Παραλλαγή της ΟΣΟ. Το while True δεν ισχυει στη ΓΛΩΣΣΑ
    plate = str(input('Δώσε αρ. κυκλοφορίας \n >>> '))
    if plate == '0':
        break #Το break δεν εφαρμόζεται στη ΓΛΩΣΣΑ
    time = float(input("Δώσε χρόνο στάθμευσης (ώρες) \n >>> ")) #Χρόνος στάθμευσης
    while time <= 0: #Έλεγχος εισόδου
        print('Παρουσιάστηκε σφάλμα. Ο χρόνος πρέπει να είναι μεγαλύτερος του 0. Δοκιμάστε ξανά')
        time = float(input("Δώσε χρόνο στάθμευσης (ώρες) \n >>> "))
    price = calc_cost(time)
    print('Το όχημα με αρ. κυκλοφορίας: ',plate,' οφείλει ',price,'€.')
    if time > 2:
        o_2h+=1
    


    
    


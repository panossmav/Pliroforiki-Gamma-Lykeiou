name = '' #Όνομα
gender = 'Β' #Φύλο
b_sugar = -1 #Σάκχαρο
b_s_boys = 0 #Αγόρια με σάκχαρο εκτός φυσιολογικών ορίων
b_s_girls = 0 #Κορίτσια με σάκχαρο εκτός φυσιολογικών ορίων
for i in range (1,90):
    while (gender != 'Α' and gender!='Κ')and(b_sugar<=0) :
        name = input('Δώσε ονοματεπώνυμο μαθητή \n >>> ')
        gender = input('Δώσε "Α" για αγόρι και "Κ" για κορίτσι \n >>> ')
        b_sugar = input('Δώσε περιεκτικότητα σακχάρου στο αίμα \n >>> ')
    if b_sugar>110 and b_sugar<70:
        print('Υψηλή περιεκτικότητα ',name,' ',gender,' ',b_sugar,'mg/dl.')
        if gender == 'Α': 
            b_s_boys+=1
        else:
            b_s_girls+=1
print('Αγόρια με σάκχαρο εκτός των ορίων: ',b_s_boys)
print('Κορίτσια με σάκχαρο εκτός των ορίων: ',b_s_girls)
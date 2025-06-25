t_tax = 0 #Συνολικ΄ός φόρος
t_n_inc = 0 #Συνολικές καθαρές απολαβές
for i in range(1,31):
    name = input('Δώσε όνομα \n >>>')
    m_inc = -1 #Μεικτές απολαβές
    while m_inc < 0 and m_inc >3000:
        m_inc=float(input('Δώσε απολαβές \n >>> '))
        if m_inc<0 and m_inc > 3000:
            print('Σφάλμα κατά την εισαγωγή: Η απολαβές πρέπει να είναι θετικός αριθμός')
    if m_inc <=700:
        tax = m_inc*0 #tax = φόρος
    elif m_inc <= 1000:
        tax = (700*0)+((m_inc-700)*0.15)
    elif m_inc <=1700:
        tax = (700*0)+(300*0.15)+((m_inc-1000)*0.3)
    else:
        tax = (700*0)+(300*0.15)+((m_inc-1700)*0.4)
    n_inc = m_inc-tax #Καθαρές απολαβές
    t_tax+=tax
    t_n_inc += n_inc
    print('Ο/Η ',name,' δέχεται: \n Μεικτές απολαβές: ',m_inc,'€. \n Φόρος: ',tax,'€. \n Καθαρές απολαβές: ',n_inc)

print('Σύνολο καθαρών απολαβών: ',t_n_inc,'€.')
print('Συνολο φόρων: ',t_tax,'€.')

    
store_code = 1 #Κωδικός καταστήματος 
l_stores = 0 #Πλήθος καταστημάτων με ζημιά
t_stores = 0 #Πλήθος συνολικών καταστημάτων
t_income = 0.0 #Συνολικά έσοδα επιχείρησης
t_expenses = 0.0 #Συνολικά έξοδα επιχείρησης
min_staff = 10^9 #Λιγότεροι υπάλληλοι
min_staff_code = 0 #Κωδικός καταστήματος λιγότερων 
while store_code != 0:
    store_code = int(input('Κωδικός καταστήματος (0 για τέλος) \n >>>'))
    if store_code == 0:
        break #ΔΕΝ ΙΣΧΥΕΙ ΓΙΑ ΓΛΩΣΣΑ
    empl = int(input('Δώσε αριθμό εργαζομένων καταστήματος \n >>>'))
    if empl<min_staff:
        min_staff = empl
        min_staff_code = store_code

    income = float(input('Δώσε έσοδα \n >>>'))
    t_income+=income
    expense = float(input('Δώσε έξοδα \n >>>'))
    t_expense+=expense
    pnl =  income-expense #Κέρδη προ φόρων
    if pnl > 0:
        tax = pnl*0.22
        net_pnl = pnl-tax #Καθαρό κέρδος
    else:
        l_stores+=1
    t_stores+=1

t_pnl = t_income - t_expense
if t_pnl>0:
    t_net_pnl = t_pnl-(t_pnl*0.22)
    print('Καθαρά κέρδη μετά φόου: %f'%t_net_pnl)
else:
    print('Συνολική ζημιά: %f'%-1*t_pnl)

print('Το κατάστημα με τους λιγότερους υπαλλήλους είναι το: %d'%min_staff_code)
if t_stores !=0:
    l_p = (l_stores/t_stores)*100
    print('Ποσοστό ζημιοφόρων καταστημάτων: %f'%l_p)

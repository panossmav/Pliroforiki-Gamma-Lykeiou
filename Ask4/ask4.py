sku = 10 #Κωδικός προϊόντος
cost = 0 #Κόστος
h_p = 0 #Προϊόντα με τιμή μεγαλύτερη των 10€ ανα τεμ.
while True:
    sku = input('Δώσε κωδικό προϊόντος \n >>> ')
    sku = int(sku)
    if sku==0:
        break
    quant = input('Δώσε ποσότητα \n >>> ')
    quant = float(quant)
    price = input('Δώσε τιμή τεμαχίου \n >>> ')
    price = float(price)
    cost+=(price*quant)
    if price > 10:
        h_p+=quant
print("Κόστος: ",cost)
if cost <= 500:
    print("ΠΛΗΡΩΜΗ ΤΟΙΣ ΜΕΤΡΗΤΗΣ \n")
else:
    i = 0
    loan = 0 #Συνολικό ποσό δόσεων
    while loan<=cost:
        installment = 20 + (i*5)
        loan+=installment
        i+=1
    print('Απαιτούνται ',i+1,' δόσεις για την εξόφληση\n')
print("Συνολικοί κωδικοί με αξία μεγαλύτερη των 10€/τμχ: ",h_p)



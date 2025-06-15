a = list(range(0,50)) #Πίνακας Α[50]
b = list(range(0,50)) #Πίνακας Β[50]
c = list(range(0,50)) #Πίνακας Γ[50]

for i in range (0,50):
    if i == 0:
        a[i]=float(input('Δώσε τον πρώτο αριθμό (Πίνακας Α)\n >>> '))
    else:
        a[i]=float(input('Δώσε τον ',i+1,'ο αριθμό (Πίνακας Α)\n >>> '))

for i in range (0,50):
    if i == 0:
        b[i]=float(input('Δώσε τον πρώτο αριθμό (Πίνακας Β)\n >>> '))
    else:
        b[i]=float(input('Δώσε τον ',i+1,'ο αριθμό (Πίνακας Β)\n >>> '))
for i in range (0,50):
    c[i] = a[i]+b[i]
    print(c[i])

    
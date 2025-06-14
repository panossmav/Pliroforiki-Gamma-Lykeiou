def max(a,b,c):
    max=-10^9 #Αρχικοποίηση μεγίστου
    if a>max:
        max = a
    if b>max:
        max = b
    if c>max:
        max = c
    return max

x = float(input("Δώσε x \n >>> "))
y = float(input("Δώσε y \n >>> "))
z = float(input("Δώσε z \n >>> "))

result = max(x,y,z)
print('Max: ',result)


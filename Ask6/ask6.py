numbers = list(range(0,250))
odd = 0 #Περριτοί
even = 0 #Άρτιοι
for i in range (0,250):
    numbers[i] = int(input("Δώσε αριθμό \n >>> "))
    if numbers[i] % 2 == 0:
        odd+=1
    else:
        even+=1
p_odd = (odd/250)*100
p_even = (even/250)*100
print("Ποσοστό περιττών: ",p_odd,'%. \n Ποσοστό άρτιων: ',p_even,'%.')
import math

def func(x,a,b):
    x=float(x)
    a=float(a)
    b=float(b)
    if x >2:
        result = (a+b)*x
    elif x < -2:
        if a < b:
            result = a
        elif b < a:
            result = b
        else:
            print('Οι αριθμοί είναι ίσοι')
            result = a
    elif -2<=x and x<2:
        if a < b:
            result = b
        elif b < a:
            result = a
        else:
            print('Οι αριθμοί είναι ίσοι')
            result = a
    else:
        result = abs(a-b)
    return result

a = input('Δώσε αριθμό α \n >>> ')
b = input('Δώσε αριθμό Β \n >>> ')
x = input('Δωσε x \n >>>')
f_result = func(x,a,b)
print(f_result)
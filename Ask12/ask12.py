phone = [None]*11000000
name = [None]*11000000

old_dig = [None]*10
new_dig = [None]*11
for i in range(11000000):
    phone[i] = int(input('Δώσε αρ. τηλεφώνου \n >>> '))
    name[i] = input('Δώσε όνομα: \n >>> ')
    for k in range(10):
        old_dig[9-k] = phone[i] % 10
        phone[i] = phone[i] // 10
    if old_dig[0] == 2:
        new_dig[0] = old_dig[0]
        new_dig[1] = old_dig[4]
        for k in range(2,11):
            new_dig[k] = old_dig[k-1]
    else:
        new_dig[0] = old_dig[0]
        new_dig[1] = old_dig[1]
        new_dig[2] = old_dig[4]
        for k in range(3,11):
            new_dig[k] = old_dig[k-1]
    print(name[i])
    for k in range(11):
        print(new_dig[k])

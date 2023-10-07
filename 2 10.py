from random import randint

n = randint(0, 20)
a = []*n
for i in range(n):
    a.append(randint(0, 20))
print(a)

product_negative = 1
summ_pos = 0
max = a[0]
b = [0]*len(a)

for i in range(len(a)):
    if a[i] > max:
        max = a[i]
    if 0 < a[i] < max:
        summ_pos += a[i]
    elif a[i] < 0:
        product_negative *= a[i]
    b[i] = a[len(a)-1-i]
for i in range(len(a)//2):
    a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i] #alternate version of the reverse array

print(a)
print(b) #revers array
print(product_negative)
print(summ_pos)

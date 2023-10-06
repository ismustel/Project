
a = [-7, 5, 4, -3, -1.2, 5, 10]
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
for i in range(len[a]): #revers an array in a different way
    a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]

print(a)
print(b) #revers array
print(product_negative)
print(summ_pos)


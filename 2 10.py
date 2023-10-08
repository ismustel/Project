from random import randint

n = randint(0, 6)
a = []*n
for i in range(n):
    a.append(randint(-20, 20))
print(a)

product_negative = 1
summ_pos = 0

b = [0]*len(a)
imax = 0

for i in range(n):
    if a[i] > a[imax]:
        imax = i

for j in range(imax):
    if a[j] > 0:
        summ_pos += a[j]

for i in range(len(a)):
    if a[i] < 0:
        product_negative *= a[i]
    b[i] = a[len(a) - 1 - i]

for j in range(imax):
    if a[j] > 0:
        summ_pos += a[j]

# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#     if 0 < a[i] < max:
#         summ_pos += a[i]
#     elif a[i] < 0:
#         product_negative *= a[i]
#     b[i] = a[len(a)-1-i]
# for i in range(len(a)//2):
#     a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i] #alternate version of the revers array

print(a)
print(b) #revers array
print(product_negative)
print(summ_pos)

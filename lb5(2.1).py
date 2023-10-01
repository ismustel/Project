from random import randint
a = []
n = int(input())
for i in range(n):
    b = randint(-100, 100)
    a.append(b)
print(a)
test = 0
product = 1
summ = 0
for i in a:
    if i == 0:
        if test == 1:
           break
        test = 1
        continue
    if test == 1:
        product *= i
        summ += i

print(product)
print(summ)
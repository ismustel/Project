from random import randint

N = int(input('N = '))
a = [(randint(0, 100)) for i in range(N)]
print(a)

left = []
right = []
for i in range(N):
    if i % 2 != 0:
        left.append(a[i])
    else:
        right.append(a[i])
print(left + right)
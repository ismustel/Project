from random import randint

m = int(input('Input number of lines: '))
n = int(input('Input number of lines: '))
a = []
for i in range(m):
    b = []
    for j in range(n):
        b.append(randint(0, 20))
    a.append(b)

for lines in a:
    print(lines)

summ_zero_lines = 0

for k in a:
    for t in range(len(k)):
        if k[t] == 0:
            summ_zero_lines += 1
print('number of lines with zero', summ_zero_lines)
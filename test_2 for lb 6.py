from random import randint

m = int(input('Input number of lines: '))
n = int(input('Input number of lines: '))
a = []

for i in range(m):
    b = []
    for j in range(n):
        b.append(randint(0, 20))
    a.append(b)
# a = [[1,2,3,4],
#      [6,2,6,1],
#      [7,2,9,1],
#      [1,4,5,6],
#      [1,4,3,1]]
print(a)

c = a[0][0]
summ_1 = 1

for i in range(4):
    summ_2 = 0
    for j in range(5):

        if c == a[j][i]:
            summ_1 += 1
        else:
            if summ_1 > 1:
                summ_2 = summ_1
            summ_1 = 1
            c = a[j][i]
        if j == 4:
            if summ_1 > summ_2:
                summ_2 = summ_1
            summ_1 = 1
    print(summ_2)

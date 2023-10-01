from math import sqrt

x = float(input('x = '))
y = float(input('y = '))
r = float(input('r = '))

if (-r) <= x <= 0 <= y >= r:
    r = (sqrt(((x + r) ** 2) + ((y - r) ** 2)))
    print('Попало')
elif 2*r >= x >= 0 >= y >= (-r):
    r = sqrt((x ** 2) + (y ** 2))
    print('Попало')
else:
    print('Не попало')








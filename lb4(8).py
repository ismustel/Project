from math import sqrt

x = float(input('x = '))
y = float(input('y = '))
r = float(input('r = '))

if (-r) <= y <= r and 0 <= x <= r:
    r = sqrt(((x - r) ** 2) + ((y - r) ** 2))
    print('Попало')
elif r <= y <= 0 and y <= (-x):
    print('Попало')
elif (-r) <= y <= 0 and y <= x:
    print('Попало')
else:
    print('Не попало')
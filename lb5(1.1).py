A = []
n = int(input())
for i in range(n):
    A.append(int(input()))
max = A[0]
for i in range(1,n):
    if A[i] > max:
        max = A[i]
imax = 0
for i in range (1,n):
    if A[i] > A[imax]:
        imax = i
print('Максимальное число:', max, 'Его номер:', imax)
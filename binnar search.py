
def search_key():
    a = [1, 2, 3, 4, 5, 6, 7]
    mid = len(a) // 2
    top = len(a) - 1
    low = 0
    search_key = int(input("Какую цифру найти: "))
    while search_key != top and low <= top:
        if a[mid] < search_key:
            low = mid + 1
        else:
            top = mid - 1
        mid = (top + low) // 2

    if low > top:
        return False
    else:
        return True

print(search_key())

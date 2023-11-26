text = input('Введите текст: ')
count_el = 0
max_count_el = 0
for let in text:
    if let == ' ':
        count_el = 0
    count_el += 1
    if count_el > max_count_el:
        max_count_el = count_el
print(max_count_el)

text = 'dasha and anna want to take apple'

symbol = input()
a = ' '
pos = 0
summ_symbol_max = 0
line = []
word_number = []
word = ''
summ_symbol = 0

for i in text:
    if i == symbol:
        summ_symbol += 1
    if i == a:
        line.append(word)
        if summ_symbol >= summ_symbol_max:
            word_number.append([word, summ_symbol])
            summ_symbol_max = summ_symbol
        summ_symbol = 0
        word = ''
    else:
        word += i

for j in word_number:
    if summ_symbol_max == j[1]:
        print('Слово', j[0])
print('Содержит символ "' + symbol + '"', str(summ_symbol_max), 'раза')








print('something')

s=int(input('Срок размещения капитала (лет):'))
k=int(input('Начальный капитал ($):'))
p=int(input('Процентная ставка (%/мес.):'))
a=int(input('Инвестиционные вливания ($/мес.):'))
print('-'*57)
print('|\t     \t|\t  основа  \t|\t сумма% \t|\t       \t|')
print('|\tмесяц\t|\tинвестиций\t|\tза месяц\t|\tкапитал\t|')
print('-'*57)
for i in range(1, s + 1):
    for p in range(1, 13):

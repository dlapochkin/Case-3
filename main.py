print('something')
sm = 0
kp = 0
s=int(input('Срок размещения капитала (лет):'))
k=int(input('Начальный капитал ($):'))
p=int(input('Процентная ставка (%/мес.):'))
a=int(input('Инвестиционные вливания ($/мес.):'))
print('-'*57)
print('|\t     \t|\t  основа  \t|\t сумма% \t|\t       \t|')
print('|\tмесяц\t|\tинвестиций\t|\tза месяц\t|\tкапитал\t|')
print('-'*57)
for p in range(1, 13):
    sm = k * p * 0.1
    kp = k + sm
    print( i, k, sm, )
    k = kp + a

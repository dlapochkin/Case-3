s=int(input('Срок размещения капитала (лет):'))
k=int(input('Начальный капитал ($):'))
p=int(input('Процентная ставка (%/мес.):'))
a=int(input('Инвестиционные вливания ($/мес.):'))
print('-'*57)
print('|\t     \t|\t  основа  \t|\t сумма% \t|\t       \t|')
print('|\tмесяц\t|\tинвестиций\t|\tза месяц\t|\tкапитал\t|')
print('-'*57)
if s == 1:
    print('1 год')
    cp = k - 1000
    for m in range(1, 13):
        k = cp + 1000
        sm = k * (p / 100)
        cp = k + sm
        print('%.2f' % k,'%.2f' % sm,'%.2f' % cp)

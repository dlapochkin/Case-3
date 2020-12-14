s=int(input('Срок размещения капитала (лет):'))
k=int(input('Начальный капитал ($):'))
p=int(input('Процентная ставка (%/мес.):'))
a=int(input('Инвестиционные вливания ($/мес.):'))
for year in range(1, s + 1):
    print(year, 'год')
    print('-' * 57)
    print('|\t     \t|\t  основа  \t|\t сумма% \t|\t       \t|')
    print('|\tмесяц\t|\tинвестиций\t|\tза месяц\t|\tкапитал\t|')
    print('-' * 57)
    if year == 1:
        cp = k - 1000
        for m in range(1, 13):
            k = cp + 1000
            sm = k * (p / 100)
            cp = k + sm
            print(m, '%.2f' % k,'%.2f' % sm,'%.2f' % cp)
    else:
        for m in range(1, 13):
            k = cp + 1000
            sm = k * (p / 100)
            cp = k + sm
            print('|     ', m, '     |', '%.2f' % k, '%.2f' % sm, '%.2f' % cp)
s = int(input('Срок размещения капитала (лет):'))
k = int(input('Начальный капитал ($):'))
p = int(input('Процентная ставка (%/мес.):'))
a = int(input('Инвестиционные вливания ($/мес.):'))
cp = k - 1000
for year in range(1, s + 1):
    print(year, 'год')
    print('-' * 57)
    print('|\t     \t|\t  основа  \t|\t сумма% \t|\t       \t|')
    print('|\tмесяц\t|\tинвестиций\t|\tза месяц\t|\tкапитал\t|')
    print('-' * 57)
    for m in range(1, 13):
        k = cp + 1000
        sm = k * (p / 100)
        cp = k + sm
        print('|\t', format(m,'2.0f'), '\t|\t', format(k, '10.2f'), '\t|\t', format(sm, '10.2f'), '\t|\t', format(cp, '10.2f'),'\t|')
    print()
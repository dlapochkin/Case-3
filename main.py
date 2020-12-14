s = int(input('Срок размещения капитала (лет):'))
k = int(input('Начальный капитал ($):'))
p = int(input('Процентная ставка (%/мес.):'))
a = int(input('Инвестиционные вливания ($/мес.):'))
cp = k - 1000
for year in range(1, s + 1):
    print(year, 'год')
    print('-' * 73)
    print('|\t',''.ljust(5),'\t|\t','основа'.ljust(10),'\t|\t','сумма%'.ljust(10),'\t|\t',''.ljust(10),'\t|')
    print('|\t','месяц','\t|\t','инвестиций'.ljust(10),'\t|\t','за месяц'.ljust(10),'\t|\t','капитал'.ljust(10),'\t|')
    print('-' * 73)
    for m in range(1, 13):
        k = cp + 1000
        sm = k * (p / 100)
        cp = k + sm
        print('|\t', format(m,'2.0f'), '\t|\t', format(k, '10.2f'), '\t|\t', format(sm, '10.2f'), '\t|\t', format(cp, '10.2f'),'\t|')
    print('-' * 73)
    print()
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада:')) #100000
per_cent.update((key,int(value * money/100)) for key, value in per_cent.items())

print("deposit =", list(per_cent.values()))
print("Максимальная сумма, которую вы можете заработать —", max (list(per_cent.values())))
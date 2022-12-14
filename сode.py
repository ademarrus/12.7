per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = input("Сколько вы планируете вложить? ")

tcb = int (float(money)*float(per_cent['ТКБ'])/100)
skb =int (float(money)*float(per_cent['СКБ'])/100)
vtb =int (float(money)*float(per_cent['ВТБ'])/100)
sber = int (float(money)*float(per_cent['СБЕР'])/100)

deposit = []

deposit.append(tcb)
deposit.append(skb)
deposit.append(vtb)
deposit.append(sber)
max_dep = max (deposit)

print(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max_dep)

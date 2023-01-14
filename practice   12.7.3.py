money=int(input("Введите вашу сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[]
deposit.append(int(money*per_cent["ТКБ"]/100))
deposit.append(int(money*per_cent["СКБ"]/100))
deposit.append(int(money*per_cent["ВТБ"]/100))
deposit.append(int(money*per_cent["СБЕР"]/100))
deposit_i="Максимальная сумма, которую вы можете заработать: "+str(max(deposit))
print(deposit)
print(deposit_i)

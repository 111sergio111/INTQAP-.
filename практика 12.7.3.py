money=int(input("Введите вашу сумму:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a=int(money*per_cent["ТКБ"]/100)
b=int(money*per_cent["СКБ"]/100)
c=int(money*per_cent["ВТБ"]/100)
d=int(money*per_cent["СБЕР"]/100)
deposit=[a,b,c,d]
print(deposit)
e="Максимальная сумма, которую вы можете заработать"" "+str(max(deposit))
print(e)
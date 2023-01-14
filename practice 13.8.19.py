tickets = int(input("Введите количество билетов:\n"))
persons=tickets
price = 0
while persons != 0:
    age = int(input(f"Введите возраст посетителя для билета № {persons}:\n "))
    if age < 18:
        print("Стоимость билета:\n Бесплатно.")
    elif 18 <= age < 25:
        price += 990
        print("Стоимость билета:\n 990 руб.")
    else:
        price += 1390
        print("Стоимость билета:\n 1390 руб.")
    persons -= 1
if tickets > 3:
    sale = price - ((price / 100) * 10)
    print(f"Сумма к оплате за билеты: \n{sale} руб.\n Была применена 10%-ая скидка за покупку более 3 билетов.")
else:
    print(f"Сумма к оплате за билеты:\n {price} руб.")

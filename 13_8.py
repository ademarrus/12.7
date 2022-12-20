count = int(input("Сколько билетов вы хотите приорести? "))
cost = 0
for i in range(count):
    age = int(input("Сколько лет посетителю? "))
    if age < 18:
        cost = cost + 0
    elif 18 <= age < 25:
        cost = cost + 990
    else:
        cost = cost + 1390
if count > 3:
    cost = cost * 0.9
print("Итого к оплате: ", round(cost), "рублей")

# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ... 1 кг конфет.
a = input("Введите цену за 1 кг конфет: ")

while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print('Неправильно ввели!')
        a = input('Введите цену 1 кг конфет: ')

i = 0.2
while i <= 1:
    cost = a * i
    print(f"Стоимость {i:.1f} кг конфет: {cost:.2f}")
    i += 0.2
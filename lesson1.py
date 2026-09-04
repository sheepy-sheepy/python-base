# 1
work = 'ha'
print(work * 7)

# 2
a = 17
b = 4

print("Деление с остатком:", a / b)
print("Деление нацело:", a // b)
print("Остаток от деления:", a % b)
print("Возведение в степень:", a ** b)

# 3
x = '2026'
y = '17.77'

x = int(x)
print(type(x))
x = float(x)
print(type(x))
y = float(y)
print(type(y))

# 4
total = 100
bonus = '50'
print('Total: ' + str(total + int(bonus)))

# 5
price = '12a'
# price = int(price)
# Возникнет ошибка невозможности преобразования строки в число,
# т.к. число содержит символ, которого нет в 10СС

# 6
# False, т.к. число 0
print(bool(0))
# True, т.к. число не 0
print(bool(1))
# False, т.к. число 0, хоть и дробное
print(bool(0.0))
# False, т.к. строка пустая
print(bool(""))
# True, т.к. строка не пустая, хоть и в ней 0
print(bool("0"))
# False, т.к. None - тип отсутствия значения
print(bool(None))

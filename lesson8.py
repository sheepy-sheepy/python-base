# 1
def print_ticket(name, film):
    print(f"Билет для {name} на фильм {film}")


print_ticket("Sheepy", "1+1")
print_ticket("Shrimp", "Ugly sister")
print_ticket("Broccoli", "Batman")


# 2
def get_square(number):
    return number ** 2


square12 = get_square(12)
print(square12 + 10)


# 3
def check_age(age):
    if age < 12:
        return "Ребенок"
    elif age <= 17:
        return "Подросток"
    return "Взрослый"


print(check_age(15))
print(check_age(61))
print(check_age(9))

# 4
city = "Moscow"


def show_city():
    city = "London"
    print(city)


show_city()  # London, т.к. помимо глобальной переменной за функцией
                # в функции есть локальная переменная city
print(city)  # Moscow, т.к. интерпретатор не видит локальную переменную в
                # функции - она существует только в функции

# 5
def get_average(*args):
    average = sum(args) / len(args)
    return average


print(get_average(1, 2, 3, 4))

# Типизация
def calc_total(price: int, quantity: int, has_discount: bool) -> int:
    total = price * quantity

    if has_discount:
        total -= 10

    return total


print(calc_total(price=15, quantity=2, has_discount=True))

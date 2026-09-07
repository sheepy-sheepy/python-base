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

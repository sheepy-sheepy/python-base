is_sunny = True
is_weekend = False

if is_sunny:
    if is_weekend:
        print("Идеальный день для прогулки")
    else:
        print("Погода хорошая, но нужно поработать")
else:
    if is_weekend:
        print("Можно остаться дома и отдохнуть")
    else:
        print("Рабочий день с плохой погодой")

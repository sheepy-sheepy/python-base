user = {"name": "Kirill", "age": 18}

try:
    email = user["email"]
except KeyError:
    raise ValueError("Ключа email нет.")
else:
    print(f"Значение ключа email: {email}")
finally:
    print("Программа завершена.")

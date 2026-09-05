user = {
    "name": "sheepy",
    "surname": "sheepy",
    "city": "Seoul"
}

print(user["name"])
print(user.get("surname"))

user["city"] = "Daegu"
user["learning_python"] = True
deleted_city = user.pop("city")

print(f"Deleted city: {deleted_city}")

for k, v in user.items():
    print(f"{k} - {v}")

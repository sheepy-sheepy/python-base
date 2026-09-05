# 1
numbers = [12, 5, 8, 99, 3, 8]

print(numbers[0], numbers[-1])
print(8 in numbers)
print(sum(numbers), max(numbers), min(numbers))

# 2
gods = ["Zeus", "Apollo", "Ares"]

gods.append("Hermes")
gods.insert(1, "Hades")
gods.remove("Apollo")
last_element = gods.pop()
print(gods, last_element)

# 3
numbers = [4, 7, 10, 15, 18, 12, 24]

for _, number in enumerate(numbers):
    if number % 2 == 0:
        print(_, number)
print(len([_ for _ in numbers if _ > 10]))

# 4
text = input("text: ")

text = text.split()
print(text)

text = "-".join(text)
print(text)

# 5
quads = [_ ** 2 for _ in range(1, 11) if _ % 3 != 0]
print(quads)

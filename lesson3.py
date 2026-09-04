# 1
for _ in range(3, 10, 3):
    print(_)

# 2
n1 = int(input("n для вывода суммы от 1 до n включительно: "))
total = 0

for _ in range(1, n1 + 1):
    total += _

print(total)

# 3
total = 0
n2 = int(
    input("n для вывода суммы от 1 до n включительно "
          "(суммируются только четные числа): "))

for _ in range(1, n2 + 1):
    if _ % 2 != 0:
        continue
    total += _

print(total)

# 4
total = 0

while True:
    num1 = int(
        input("Введите число для суммирования. Для завершения введите 0.: "))
    if num1 == 0:
        break
    total += num1

print(total)

# 5
total = 0

for _ in range(10):
    num2 = int(input(f"Ведите число №{_ + 1}/10. Для завершения введите "
                     f"отрицательное число.: "))
    if num2 < 0:
        break
    total += num2

print(total)

# 6
for _ in range(1, 30 + 1):
    if _ % 3 == 0:
        continue
    print(_)

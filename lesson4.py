# 1
message = input("Строка message: ")

if not message.strip():
    print("EMPTY")
elif "spam" in message.lower():
    print("BLOCKED")

# 2
s = input("Строка s: ")
i = int(input("Число i: "))

if -len(s) <= i < len(s):
    print(s[i])
    print(s[i].lower() in ["a", "а"])
else:
    print("IndexError")

# 3
full_name = input("full_name: ").strip().title()

print(f"{full_name[0]}.{full_name[len(full_name) - 1]}")

# 1
student = ("Sheepy", 12, "Spanish")
name, age, language = student

print(f"name: {name},\n"
      f"age: {age},\n"
      f"language: {language}")

# 2
words = ["python", "code", "list", "python", "set", "code", "tuple"]
unique_words = set(words)

print(unique_words)
print(f"Есть ли слово 'tuple' в множестве? - {'tuple' in unique_words}")

unique_words.add("loop")
unique_words.remove("list")

print(unique_words)

# 1
class GameCharacter:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

    def attack(self):
        print(f"{self.name} наносит {self.damage} урона")

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} получил {amount} урона. "
              f"Осталось здоровья: {self.health}")


sheepy = GameCharacter("Sheepy", 20, 100)
sheepy.attack()
for _ in range(5):
    sheepy.take_damage(8)


# 2
class Cart:
    def __init__(self, owner):
        self.owner = owner
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name,
                           "price": price})

    def get_total(self):
        return sum(item["price"] for item in self.items)

    def show_items(self):
        if not self.items:
            print("Корзина пуста")
            return
        for item in self.items:
            print(f"{item["name"]} - {item["price"]}")


my_cart = Cart("Sheepy")
print(my_cart.get_total())
my_cart.show_items()
my_cart.add_item("sushi set", 20)
my_cart.add_item("dinozzor", 4)
my_cart.show_items()
print(my_cart.get_total())

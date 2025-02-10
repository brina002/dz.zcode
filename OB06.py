import random

# Класс Вредителя
class Pest:
    def __init__(self, name, pest_type):
        self.name = name
        self.type = pest_type  # Тип вредителя: "insect" или "fungus"
        self.health = 100
        self.attack_power = 20
        self.can_attack = True  # Возможность атаковать

    def attack(self, plant):
        if self.can_attack:
            damage = self.attack_power
            plant.health -= damage
            print(f"{self.name} атакует {plant.name}, нанося {damage} урона. Здоровье {plant.name}: {plant.health}")
        else:
            print(f"{self.name} временно не может атаковать!")
            self.can_attack = True  # Восстановить возможность атаки в следующем раунде

    def is_alive(self):
        return self.health > 0

# Класс Растения
class Plant:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

# Класс Фермера
class Farmer:
    def __init__(self, name):
        self.name = name
        self.defense_items = {
            1: ("Инсектицид", "insect", 50),
            2: ("Фунгицид", "fungus", 34),
            3: ("Биологическое средство", "both", 25)
        }

    def use_defense_item(self, choice, pest):
        if choice in self.defense_items:
            item_name, effective_type, damage = self.defense_items[choice]
            if effective_type == pest.type or effective_type == "both":
                pest.health -= damage
                pest.can_attack = False  # Заблокировать атаку вредителя в следующем раунде
                print(f"{self.name} использует {item_name} против {pest.name}, нанося {damage} урона. Здоровье {pest.name}: {pest.health}")
            else:
                pest.health = 100  # Полное восстановление здоровья вредителя
                print(f"{item_name} неэффективен против {pest.name}! Вредитель восстанавливается. Здоровье {pest.name}: {pest.health}")
        else:
            print("Неверный выбор!")

    def choose_defense_item(self):
        print("Доступные средства защиты:")
        for key, (item, pest_type, damage) in self.defense_items.items():
            print(f"{key}. {item} (эффективно против: {pest_type}, урон: {damage})")
        try:
            choice = int(input("Выберите номер средства защиты: "))
        except ValueError:
            choice = 0  # Неверный выбор
        return choice

# Класс Игры
class Game:
    def __init__(self, farmer, pest, plant):
        self.farmer = farmer
        self.pest = pest
        self.plant = plant

    def start(self):
        print("Игра началась! Защищайте растение от вредителя.")

        while self.plant.is_alive() and self.pest.is_alive():
            # Ход вредителя
            print("\nХод вредителя:")
            self.pest.attack(self.plant)

            if not self.plant.is_alive():
                print(f"{self.plant.name} уничтожено! Вы проиграли!")
                break

            # Ход фермера
            print("\nХод фермера:")
            defense_choice = self.farmer.choose_defense_item()
            self.farmer.use_defense_item(defense_choice, self.pest)

            if not self.pest.is_alive():
                print(f"{self.pest.name} уничтожен! Вы победили!")
                break

# Основной код
if __name__ == "__main__":
    farmer_name = input("Введите имя фермера: ")
    plant_name = input("Введите название растения: ")
    pest_data = random.choice([
        ("Тля", "insect"),
        ("Колорадский жук", "insect"),
        ("Фузариоз", "fungus"),
        ("Мучнистая роса", "fungus")
    ])
    pest_name, pest_type = pest_data

    farmer = Farmer(farmer_name)
    plant = Plant(plant_name)
    pest = Pest(pest_name, pest_type)

    print(f"Ваш противник: {pest_name} (тип: {pest_type})")
    game = Game(farmer, pest, plant)
    game.start()

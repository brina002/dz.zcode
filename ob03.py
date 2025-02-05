# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

def make_sound(self):
    return "Some generic sound."

def eat (self):
    pass


# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).

class Bird(Animal):
    def __init__(self, name, age, wing_span): # 1 specific attribute
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "chirp-chirp"


class Mammal(Animal):
    def __init__(self, name, age, weight): # 1 specific attribute
        super().__init__(name, age)
        self.weight = weight

    def make_sound(self):
        return "rrr"


class Reptile(Animal):
    def __init__(self, name, age, length):  # 1 specific attribute
        super().__init__(name, age)
        self.length = length

    def make_sound(self):
        return "hsss"


# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()`
# для каждого животного.

def animal_sound(animals):
    for animal in animals:
            print(animal.make_sound())

# 4. Используйте композицию для создания класса `Zoo`, который будет
# содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Animal {animal.name} added to the zoo.")


    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {type(employee).__name__} added to the zoo.")


# 5. Создайте классы для сотрудников, например, `ZooKeeper`,
# `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class ZooKeeper():
    def feed_animal(self, animal):
        print(f'Zookeeper is feeding the {animal.name}.')

class Veterinarian():
    def heal_animal(self, animal):
        print(f'Veterinarian is healing the {animal.name}.')

bird1 = Bird("Pigeon", 1, 0.5)
mammal1 = Mammal("Lion", 3, 15)
reptile1 = Reptile("Snake", 4, 2)

zoo = Zoo("Park")
zookeeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

animal_sound(zoo.animals)

zookeeper.feed_animal(bird1)
veterinarian.heal_animal(reptile1)








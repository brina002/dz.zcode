class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Some generic sound"

    def eat(self):
        return f"{self.name} is eating."

    def __repr__(self):
        return f"Animal(Name: {self.name}, Age: {self.age})"


class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span  # Специфический атрибут для птиц

    def make_sound(self):
        return "Chirp chirp!"

    def fly(self):
        return f"{self.name} is flying with a wingspan of {self.wing_span} meters."

    def __repr__(self):
        return f"Bird(Name: {self.name}, Age: {self.age}, Wing Span: {self.wing_span}m)"


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # Специфический атрибут для млекопитающих

    def make_sound(self):
        return "Growl or grunt!"

    def run(self):
        return f"{self.name} is running."

    def __repr__(self):
        return f"Mammal(Name: {self.name}, Age: {self.age}, Fur Color: {self.fur_color})"


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type  # Специфический атрибут для рептилий

    def make_sound(self):
        return "Hiss!"

    def crawl(self):
        return f"{self.name} is crawling."

    def __repr__(self):
        return f"Reptile(Name: {self.name}, Age: {self.age}, Scale Type: {self.scale_type})"


# Пример использования
if __name__ == "__main__":
    # Создаем экземпляры различных животных
    parrot = Bird(name="Parrot", age=2, wing_span=0.5)
    lion = Mammal(name="Lion", age=4, fur_color="Golden")
    snake = Reptile(name="Snake", age=3, scale_type="Smooth")

    # Используем методы базового и производного классов
    print(parrot)  # Bird(Name: Parrot, Age: 2, Wing Span: 0.5m)
    print(parrot.make_sound())  # Chirp chirp!
    print(parrot.fly())  # Parrot is flying with a wingspan of 0.5 meters.
    print(parrot.eat())  # Parrot is eating.

    print(lion)  # Mammal(Name: Lion, Age: 4, Fur Color: Golden)
    print(lion.make_sound())  # Growl or grunt!
    print(lion.run())  # Lion is running.
    print(lion.eat())  # Lion is eating.

    print(snake)  # Reptile(Name: Snake, Age: 3, Scale Type: Smooth)
    print(snake.make_sound())  # Hiss!
    print(snake.crawl())  # Snake is crawling.
    print(snake.eat())  # Snake is eating.

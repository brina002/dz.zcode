from abc import ABC, abstractmethod


# Шаг 1: Создание абстрактного класса ProtectionMethod
class ProtectionMethod(ABC):
    @abstractmethod
    def apply_protection(self):
        pass


# Шаг 2: Реализация конкретных типов защиты
class Insecticide(ProtectionMethod):
    def apply_protection(self):
        print("Работник наносит инсектицид для защиты от насекомых.")


class Fungicide(ProtectionMethod):
    def apply_protection(self):
        print("Работник применяет фунгицид для защиты от грибков.")


# Шаг 3: Модификация класса Farmer
class Farmer:
    def __init__(self, name):
        self.name = name
        self.protection_method = None

    def change_protection(self, protection_method: ProtectionMethod):
        self.protection_method = protection_method
        print(f"{self.name} выбирает {protection_method.__class__.__name__}.")

    def apply_protection(self):
        if self.protection_method:
            self.protection_method.apply_protection()
            print("Вредитель побежден!")
        else:
            print("Метод защиты не выбран.")


# Шаг 4: Реализация демонстрации
if __name__ == "__main__":
    farmer = Farmer("Иван")

    # Выбор инсектицида
    insecticide = Insecticide()
    farmer.change_protection(insecticide)
    farmer.apply_protection()

    print()  # Разделение для читаемости

    # Выбор фунгицида
    fungicide = Fungicide()
    farmer.change_protection(fungicide)
    farmer.apply_protection()



# Задача: Разработать простую игру, в которой пользователь может выбирать различные 
# методы защиты сельскохозяйственных культур от вредителей. 
# Программа должна быть спроектирована таким образом,
# чтобы легко можно было добавлять новые методы защиты, не изменяя существующий код
# для сельскохозяйственных работ или механизмы защиты.
# Исходные данные:
# Есть класс Farmer, представляющий работника сельского хозяйства.
# Есть класс Pest, представляющий вредителя.
# Работник может выбирать метод защиты для своих культур.

# Шаг 1: Создайте абстрактный класс для методов защиты
# Создайте абстрактный класс ProtectionMethod, 
# который будет содержать абстрактный метод apply_protection().
# Шаг 2: Реализуйте конкретные типы защиты
# Создайте несколько классов, унаследованных от ProtectionMethod, например, 
# Insecticide (инсектицид) и Fungicide (фунгицид). 
# Каждый из этих классов реализует метод apply_protection() своим уникальным способом 
# (например, распыление или обработка почвы).
# Шаг 3: Модифицируйте класс Farmer
# Добавьте в класс Farmer поле, которое будет хранить объект класса ProtectionMethod.
# Добавьте метод change_protection(), который позволяет изменить метод защиты для растения.
# Шаг 4: Реализация защиты
# Реализуйте простой механизм для демонстрации применения защиты от вредителей, 
# исходя из выбранного метода. Работник может выбрать инсектицид, фунгицид 
# или другие методы для обработки своих культур в зависимости от типа вредителя.

# Требования к заданию:
# - Программа должна демонстрировать применение принципа открытости/закрытости:
# новые типы защиты можно легко добавлять, не изменяя существующие классы фермеров и механизм защиты.
# - Программа должна выводить результат защиты в консоль.
  
# Пример результата:
# Фермер выбирает инсектицид.
# Работник наносит инсектицид для защиты от насекомых.
# Вредитель побежден!
# 
# Фермер выбирает фунгицид.
# Работник применяет фунгицид для защиты от грибков.
# Вредитель побежден!
#
# Фермер выбирает биологический контроль.
# Работник вводит естественных хищников для борьбы с вредителями.
# Вредитель побежден!

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

class BiologicalControl(ProtectionMethod):
    def apply_protection(self):
        print("Работник вводит естественных хищников для борьбы с вредителями.")

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

    print() 

    # Выбор фунгицида
    fungicide = Fungicide()
    farmer.change_protection(fungicide)
    farmer.apply_protection()

    print() 

    # Выбор биологического контроля
    biological_control = BiologicalControl()
    farmer.change_protection(biological_control)
    farmer.apply_protection()



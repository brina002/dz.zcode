class Store:
    def __init__(self, name, address):
        """Инициализация магазина с названием, адресом и пустым ассортиментом."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент или обновляет его цену."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен/обновлен с ценой {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара или None, если его нет."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")


# Создание нескольких магазинов
stores = [
    Store("Магазин №1", "ул. Пушкина, 10"),
    Store("Супермаркет", "пр. Ленина, 25"),
    Store("Мини-маркет", "ул. Советская, 3"),
    Store("Магазин у дома", "ул. Горького, 15"),
    Store("Гипермаркет", "ул. Победы, 50"),
]


# Меню для пользователя
def user_menu():
    while True:
        print("\nСписок магазинов:")
        for i, store in enumerate(stores, start=1):
            print(f"{i}. {store.name} ({store.address})")
        print("0. Выйти")

        try:
            store_choice = int(input("Введите номер магазина для управления: "))
            if store_choice == 0:
                print("Спасибо за использование программы! До свидания!")
                break
            if not 1 <= store_choice <= len(stores):
                print("Некорректный выбор. Попробуйте снова.")
                continue

            selected_store = stores[store_choice - 1]
            print(f"\nВы выбрали магазин: {selected_store.name}, Адрес: {selected_store.address}")
            store_actions(selected_store)

        except ValueError:
            print("Ошибка: введите корректное число.")

def store_actions(store):
    while True:
        print(f"\nУправление магазином: {store.name}")
        print("1. Добавить товары")
        print("2. Удалить товар")
        print("3. Узнать цену товара")
        print("4. Обновить цену товара")
        print("5. Показать весь ассортимент")
        print("6. Применить изменения товара ко всем магазинам")
        print("0. Вернуться к выбору магазина")

        choice = input("Ваш выбор: ")

        if choice == "1":
            print("Введите товары и их цены (введите 'стоп' для завершения):")
            while True:
                item_name = input("Название товара: ")
                if item_name.lower() == "стоп":
                    break
                try:
                    price = float(input("Цена товара "))
                    store.add_item(item_name, price)
                except ValueError:
                    print("Ошибка: цена должна быть числом.")

        elif choice == "2":
            item_name = input("Введите название товара для удаления: ")
            store.remove_item(item_name)

        elif choice == "3":
            item_name = input("Введите название товара для поиска цены: ")
            price = store.get_price(item_name)
            if price is not None:
                print(f"Цена товара '{item_name}': {price}")
            else:
                print(f"Товар '{item_name}' отсутствует в ассортименте.")

        elif choice == "4":
            item_name = input("Введите название товара для обновления цены: ")
            try:
                new_price = float(input("Введите новую цену товара: "))
                store.update_price(item_name, new_price)
            except ValueError:
                print("Ошибка: цена должна быть числом.")

        elif choice == "5":
            print("Текущий ассортимент магазина:")
            for item, price in store.items.items():
                print(f"- {item}: {price}")
            if not store.items:
                print("Ассортимент пуст.")

        elif choice == "6":
            item_name = input("Введите название товара для добавления/обновления во всех магазинах: ")
            try:
                price = float(input("Введите цену товара: "))
                for s in stores:
                    s.add_item(item_name, price)
                print(f"Товар '{item_name}' добавлен/обновлен во всех магазинах с ценой {price}.")
            except ValueError:
                print("Ошибка: цена должна быть числом.")

        elif choice == "0":
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

# Запуск программы
user_menu()
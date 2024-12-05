class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self.__access_level = access_level

    # Getters
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self.__access_level

    # Setters (если нужно разрешить изменение имени)
    def set_name(self, name):
        self._name = name

    # Представление объекта в читаемом формате
    def __repr__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name, admin_access_level='admin'):
        super().__init__(user_id, name, access_level='admin')
        self.__admin_access_level = admin_access_level
        self._users = []  # Список пользователей

    # Добавление пользователя
    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Invalid user type. Cannot add.")

    # Удаление пользователя по ID
    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"User {user.get_name()} removed.")
                return
        print(f"User with ID {user_id} not found.")

    # Получение списка пользователей
    def get_all_users(self):
        return self._users

    # Представление объекта Admin
    def __repr__(self):
        return f"Admin(ID: {self.get_user_id()}, Name: {self.get_name()}, Access Level: {self.get_access_level()})"


# Пример использования
if __name__ == "__main__":
    # Создаем администратора
    admin = Admin(user_id=1, name="Sasha")

    # Создаем пользователей
    user1 = User(user_id=2, name="Masha")
    user2 = User(user_id=3, name="Dasha")

    # Администратор добавляет пользователей
    admin.add_user(user1)
    admin.add_user(user2)

    # Просмотр всех пользователей
    print("All Users:", admin.get_all_users())

    # Удаление пользователя
    admin.remove_user(2)

    # Проверка обновленного списка пользователей
    print("Updated Users:", admin.get_all_users())

class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    # Getter and Setter methods for user_id
    def get_user_id(self):
        return self._user_id

    def set_user_id(self, user_id):
        self._user_id = user_id

    # Getter and Setter methods for name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter for access_level
    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, user_list, user):
        if user not in user_list:
            user_list.append(user)
            print(f'User {user.get_name()} added successfully.')
        else:
            print('User already exists.')

    def remove_user(self, user_list, user):
        if user in user_list:
            user_list.remove(user)
            print(f'User {user.get_name()} removed successfully.')
        else:
            print('User not found.')


# Example Usage
if __name__ == '__main__':
    # Создание списка пользователей
    user_list = []

    # Создаем обычного пользователя и администратора
    user1 = User('001', 'John Doe')
    admin1 = Admin('002', 'Jane Doe')

    # Администратор добавляет пользователей
    admin1.add_user(user_list, user1)
    admin1.add_user(user_list, admin1)

    # Вывод информации о пользователях
    for user in user_list:
        print(f'ID: {user.get_user_id()}, Name: {user.get_name()}, Access Level: {user.get_access_level()}')

    # Администратор удаляет пользователя
    admin1.remove_user(user_list, user1)

    # Вывод текущего списка пользователей
    print("\nCurrent Users after deletion:")
    for user in user_list:
        print(f'ID: {user.get_user_id()}, Name: {user.get_name()}')

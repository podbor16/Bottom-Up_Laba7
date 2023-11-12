"""Программа для добавления судов в реестр"""

class Ship:
    """Родительский класс"""
    def __init__(self, name, length, max_speed):
        """Инициализация атрибутов класса"""
        self.__name = name
        self.__length = length
        self.__max_speed = max_speed

    @property
    def name(self):
        """"Функция, считывающая имя корабля"""
        return self.__name

    @property
    def length(self):
        """"Функция, считывающая длину палубы"""
        return self.__length

    @property
    def max_speed(self):
        """"Функция, считывающая максимальную скорость"""
        return self.__max_speed

    def display_info(self):
        """Функция для переопределения вывода информации на экран"""
        pass

class Steamship(Ship):
    """"Дочерний класс для парохода"""
    def __init__(self, name, length, max_speed, engine_type):
        """Инициализация атрибутов класса"""
        super().__init__(name, length, max_speed)
        # super() для того, чтобы вызвать конструктор родительского класса
        # (Ship) и выполнить необходимую инициализацию родительских атрибутов.
        self.__engine_type = engine_type

    @property
    def engine_type(self):
        """Функция, считывающая тип двигателя"""
        return self.__engine_type


    def display_info(self):
        """Функция для вывода информации о параходе на экран"""
        print(f"\nТип: Пароход")
        print(f"Имя: {self.name}")
        print(f"Длина: {self.length} метров")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Тип двигателя: {self.engine_type}")

class SailingShip(Ship):
    """Дочерний класс для определения парусника"""
    def __init__(self, name, length, max_speed, mast_count):
        """Инициализация атрибутов класса"""
        super().__init__(name, length, max_speed)
        self.__mast_count = mast_count

    @property
    def mast_count(self):
        """Функция, считывающая количество мачт"""
        return self.__mast_count

    def display_info(self):
        """Функция для вывода информации о паруснике на экран"""
        print(f"\nТип: Парусник")
        print(f"Имя: {self.name}")
        print(f"Длина: {self.length} метров")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Количество мачт: {self.mast_count}")

class Corvette(Ship):
    """Дочерний класс для определения корвета"""
    def __init__(self, name, length, max_speed, weapon):
        """Инициализация атрибутов класса"""
        super().__init__(name, length, max_speed)
        self.__weapon = weapon

    @property
    def weapon(self):
        """Функция, считывающая вооружение корвета"""
        return self.__weapon

    def display_info(self):
        """Функция для вывода информации о паруснике на экран"""
        print(f"\nТип: Корвет")
        print(f"Имя: {self.name}")
        print(f"Длина: {self.length} метров")
        print(f"Максимальная скорость: {self.max_speed} км/ч")
        print(f"Вооружение: {self.weapon}")

def add_ship_to_registry(ship_list, ship):
    """Функция добавления судна в реесстр"""
    ship_list.append(ship)

def display_registry_contents(ship_list):
    """Функция для вывода реестра судов"""
    for index, ship in enumerate(ship_list, start=1):
        print(f"{index}. {ship.name}")

def demonstrate_skills(ship):
    """Функция вывода информации о судне"""
    ship.display_info()

def main():
    """Главная функция программы с меню"""
    ship_list = []
    while True:
        print("\nОпции:")
        print("1. Добавить судно")
        print("2. Показать реестр судов")
        print("3. Выход")
        choice = int(input("Введите ваш выбор: "))

        if choice == 1:
            name = input("\nВведите имя судна: ")
            while True:
                length = input("Введите длину судна (в метрах): ")
                if length.isdigit():
                    break
                else:
                    print("Ошибка! Введите длину судна цифрами")
            while True:
                max_speed = input("Введите максимальную скорость судна (в км/ч): ")
                if max_speed.isdigit():
                    break
                else:
                    print("Ошибка! Введите максимальную скорость судна цифрами")

            print("\nВыберите тип судна:")
            print("1. Пароход")
            print("2. Парусник")
            print("3. Корвет")
            ship_type_choice = input("Введите номер выбранного типа: ")

            if ship_type_choice == "1":
                engine_type = input("Введите тип двигателя парохода: ")
                ship = Steamship(name, length, max_speed, engine_type)
            elif ship_type_choice == "2":
                mast_count = input("Введите количество мачт парусника: ")
                ship = SailingShip(name, length, max_speed, mast_count)
            elif ship_type_choice == "3":
                weapon = input("Введите вооружение корвета: ")
                ship = Corvette(name, length, max_speed, weapon)
            else:
                print("Неверный выбор типа судна.")
                continue

            add_ship_to_registry(ship_list, ship)
            print(f"\nСудно '{name}' успешно добавлено в реестр.")

        elif choice == 2:
            if len(ship_list) != 0:
                print("\nВыберите судно для демонстрации данных о нём:")
                display_registry_contents(ship_list)

                try:
                    selected_index = int(input("Введите номер судна: ")) - 1
                    if 0 <= selected_index < len(ship_list):
                        selected_ship = ship_list[selected_index]
                        demonstrate_skills(selected_ship)
                        input("\nНажмите Enter, чтобы продолжить...")
                    else:
                        print("Неверный номер судна.")
                except ValueError:
                    print("Введите число.")
            else:
                print("Реестр пуст.")
                input("\nНажмите Enter, чтобы продолжить...")

        elif choice == 3:
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите допустимую опцию.")

if __name__ == "__main__":
    main()

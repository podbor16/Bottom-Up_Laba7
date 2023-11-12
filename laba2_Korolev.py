class Ship:
    def __init__(self, name, length, max_speed):
        self.__name = name
        self.__length = length
        self.__max_speed = max_speed

    @property
    def name(self):
        return self.__name

    @property
    def length(self):
        return self.__length

    @property
    def max_speed(self):
        return self.__max_speed

class Steamship(Ship):
    def __init__(self, name, length, max_speed, engine_type):
        super().__init__(name, length, max_speed)
        # super() для того, чтобы вызвать конструктор родительского класса
        # (Ship) и выполнить необходимую инициализацию родительских атрибутов.
        self.__engine_type = engine_type

    @property
    def engine_type(self):
        return self.__engine_type

class SailingShip(Ship):
    def __init__(self, name, length, max_speed, mast_count):
        super().__init__(name, length, max_speed)
        self.__mast_count = mast_count

    @property
    def mast_count(self):
        return self.__mast_count

class Corvette(Ship):
    def __init__(self, name, length, max_speed, weapon):
        super().__init__(name, length, max_speed)
        self.__weapon = weapon

    @property
    def weapon(self):
        return self.__weapon



string_ = 'Привет'


class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int) == False or isinstance(other, House) == False:
            return print('Элемент не принадлетиж к классу House, либо не является типа int')

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        elif isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int) == False or isinstance(other, House) == False:
            return print('Элемент не принадлетиж к классу House, либо не является типа int')

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        elif isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int) == False or isinstance(other, House) == False:
            return print('Элемент не принадлетиж к классу House, либо не является типа int')

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value
        elif isinstance(value, House):
            return self.number_of_floors + value.number_of_floors
        elif isinstance(value, int) == False or isinstance(value, House) == False:
            return print('Элемент не принадлетиж к классу House, либо не является типа int')

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


Korp1 = House('Волга', 15)
Korp2 = House('Долг', 15)
print('Одинаковое кол-во этажей:', Korp1 == Korp2)
print('Меньше:', Korp1 < Korp2)
print('Меньше либо равно:', Korp1 <= Korp2)
print('Больше:', Korp1 > Korp2)
print('Больше либо равно:', Korp1 >= Korp2)
print('Не равно:', Korp1 != Korp2)
print('Увеличить кол-во этажей, add:', Korp1 + 2)
print('Увеличить кол-во этажей, radd:', 2 + Korp1)
Korp1 += 2
print('Увеличить кол-во этажей, iadd:', Korp1)
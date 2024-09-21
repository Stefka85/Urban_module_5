#   Задача "Нужно больше этажей"

class House:
    def __init__(self, name, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor: int):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other.number_of_floors, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self


dom1 = House('ЖК Эльбрус', 10)
dom2 = House('ЖК Акация', 20)
print(dom1)
print(dom2)

print(dom1 == dom2) # __eq__

dom1 = dom1 + 10 # __add__
print(dom1)
print(dom1 == dom2)

dom1 += 10 # __iadd__
print(dom1)

dom2 = 10 + dom2 # __radd__
print(dom2)

print(dom1 > dom2) # __gt__
print(dom1 >= dom2) # __ge__
print(dom1 < dom2) # __lt__
print(dom1 <= dom2) # __le__
print(dom1 != dom2) # __ne__
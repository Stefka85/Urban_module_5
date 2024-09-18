#   Задача "Магические здания"

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

dom1 = House('ЖК Эльбрус', 10)
dom2 = House('ЖК Акация', 20)
print(dom1)
print(dom2)

print(len(dom1))
print(len(dom2))



#   Задача "Developer - не только разработчик"

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


dom = House('ЖК Эльбрус,', 30)
dom1 = House('ЖК Горский', 18)
dom2 = House('Домик в деревне', 2)
dom.go_to(31)
dom1.go_to(5)
dom2.go_to(10)
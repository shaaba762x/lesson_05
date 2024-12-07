class Hause:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor <= 0:
           print(f'в {self.name} подвала нет и мы никуда не едем.')
        elif self.new_floor <= self.number_of_floors:
            for floor in range(1, self.new_floor+1):
                print(floor)
                if floor == self.number_of_floors:
                    print(f'Мы поднялись на {self.new_floor} этаж.')
                    return
        else:
            print(f'В {self.name} всего {self.number_of_floors} этажей. Выше не уехать.')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}."


h1 = Hause('ТЦ "Вавилон"', 122)
h2 = Hause('ТЦ "Башня"', 5)
_a = (int(input(f'Введите номер этажа на который хотите подняться: ',)))
h1.go_to(_a)
h2.go_to(_a)

print(h1)
print(h2)
print(len(h1))
print(len(h2))

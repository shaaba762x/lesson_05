class hause:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor <= self.number_of_floors:
            for floor in range(1, self.new_floor):
                print(floor)
                if floor == self.number_of_floors:
                    print(floor)
                    print(f'Мы поднялись на {self.new_floor} этаж.')
                    return
        else:
            print(f'В {self.name} всего {self.number_of_floors} этажей. Выше не уехать.')


h1 = hause('ТЦ "Вавилон",', 122)
h2 = hause('ТЦ "Башня",', 5)
print(h1.name,'Этажей -',h1.number_of_floors)
print(h2.name,'Этажей -',h2.number_of_floors)
_a = (int(input(f'Введите номер этажа на который хотите подняться: ',)))
h1.go_to(_a)
h2.go_to(_a)
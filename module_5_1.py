class hause:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor <= self.number_of_floors:
            for floor in range(1, self.new_floor+1):
                print(floor)
                if floor == self.number_of_floors:
                    print(f'Мы поднялись на {self.new_floor} этаж.')
                    return
        else:
            print(f'В {self.name} всего {self.number_of_floors} этажей. Выше не уехать.')

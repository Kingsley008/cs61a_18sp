class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return self.make + ' ' + self.model + ' cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return self.make + ' ' + self.model + ' gas level: ' + str(self.gas)


class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return Car.drive(self)


class FoodTruck(MonsterTruck):
    delicious = 'meh'

    def serve(self):
        if FoodTruck.size == 'delicious':
            print('Yum!')
        if self.food != 'Tacos':
            return 'But no tacos...'
        else:
            return 'Mmm!'


taco_truck = FoodTruck('Tacos', 'Truck')
taco_truck.food = 'Guacamole'
taco_truck.serve()
taco_truck.food = taco_truck.make
FoodTruck.size = taco_truck.delicious
taco_truck.serve()
taco_truck.size = 'delicious'
taco_truck.serve()
# FoodTruck.pop_tire()
a = FoodTruck.pop_tire(taco_truck)


a = taco_truck.drive()
print(a)
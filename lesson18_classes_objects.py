# Lesson 18 - Creating objects with classes

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Vehicles move.')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model S')
# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()


# These classes inherit from the Vehicle class.
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        # super().__init__(make, model): This means we're going to inherit the make and model from the parent class.
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along...')


class Truck(Vehicle):
    def moves(self):
        print('Trucks roll down the road.')


class GolfCart(Vehicle):
    pass  # This is a placeholder that allows the class to be empty.


cessna = Airplane('Cessna', 'Skyhawk', 'N123')
cessna.get_make_model()
cessna.moves()

mack = Truck('Mack', 'Pinnacle')
mack.get_make_model()
mack.moves()

golfWagon = GolfCart('Yamaha', 'GC100')
golfWagon.get_make_model()
golfWagon.moves()

print('\n\n')

# Polymorphism: The ability to present the same interface for different data types.
for v in (my_car, your_car, cessna, mack, golfWagon):
    v.get_make_model()
    v.moves()
    print('\n')

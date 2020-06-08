class InvalidCarExeption(Exception):
    def __init__(self,message,errors):
        super().__init__(message)
        self.errors = errors
        # Display the errors
        print("Error: {} {}".format(message,errors))


class Car:
    def __init__(self, pax_count, car_mass,gear_count):
        self.pax_count = pax_count
        self.car_mass = car_mass
        self.gear_count = gear_count
        if pax_count not in range(1,5):
           raise InvalidCarExeption('Pax_count out of range','InvalidPaxCountError')
        elif car_mass > 2000:
            raise InvalidCarExeption('Car_mass out of range','InvalidCarMassError')
        else:
            print("Car added successfully!")

    def __setattr__(self, name, value):
        if name == "pax_count" and value not in range(1,5):
            raise InvalidCarExeption('Pax_count out of range','InvalidPaxCountError')
        elif name == "car_mass" and value > 2000:
            raise InvalidCarExeption('Car_mass out of range','InvalidCarMassError')

    def total_mass(self):
        return self.car_mass
    
c = Car(3,2000,1)
c.pax_count = 6



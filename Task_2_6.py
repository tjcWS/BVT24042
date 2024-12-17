class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return 'Марка: {}, модель: {}'.format(self.make, self.model)
    
class Car(Vehicle):
    def __init__(self, make, model):
        Vehicle.__init__(self, make, model)
        self.typeF = 0 
    def fuel_type(self, typeF):
        self.typeF = typeF 
        return 'установлен тип топлива.'
    def get_info(self):
        return 'Марка: {}, модель: {}, тип топлива: {}'.format(self.make, self.model, self.typeF)

obj = Vehicle('Audi', 's7')
print(obj.get_info())

obj1 = Car('Audi', 's7')
print(obj1.fuel_type(92))
print(obj1.get_info())





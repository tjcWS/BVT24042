class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return 'Радиус круга: {}'.format(self.radius)
    
    def set_radius(self, new_radius):
        self.radius = new_radius
        return 'Новый радиус: {}'.format(self.radius)
    
circle = Circle(16)
print(circle.get_radius())
print(circle.set_radius(20))
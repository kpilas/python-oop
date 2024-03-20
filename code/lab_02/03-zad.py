class Rectangle:
    def __init__(self, length, width):
        self.lengh = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width


    def __repr__(self):
        return f'{type(self).__name__}({', '.join(str(k)+ ' = ' + str(v) for k,v in self.__dict__.items())})'

r = Rectangle(3, 4)

print(r)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.x = 6
        # print(self.__init__.__code__.co_varnames[1:])

    @property
    def area(self):
        return self.length * self.width

    def __str__(self):
        return f'{type(self).__name__}:\ndługość: {self.length}\nszerokość: {self.width}\npole: {self.area}'

    def __repr__(self):
        return (f'{type(self).__name__}'
                f'({', '.join(str(n) + ' = ' + str(self.__dict__[n]) for n in self.__init__.__code__.co_varnames[1:])})')


class Cuboid(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    @property
    def area(self):
        return 2 * (super().area + self.width * self.height + self.length * self.height)

    @property
    def volume(self):
        return super().area * self.height

    def __str__(self):
        return super().__str__() + f'\nwysokość: {self.height}\nobjętość: {self.volume}'


r = Rectangle(3, 4)
c = Cuboid(3, 4, 5)
# print(repr(c))
# print(c)


class InvalidData(Exception): pass

with open('dane.txt', 'r', encoding='utf8') as ff:
    for row in ff:
        text_list = row.split()
        try:
            # number_list = [float(x) for x in text_list]
            number_list = list(map(float, text_list))
            if number_list[0] == 1 and len(number_list) == 3:
                if all(map(lambda x: x > 0, number_list[1:])):
                    r = Rectangle(*number_list[1:])
                    print(r)
                    print('-' * 15)
                else:
                    raise InvalidData('Ujemne wartości!')

            elif number_list[0] == 2 and len(number_list) == 4:
                if all(map(lambda x: x > 0, number_list[1:])):
                    c = Cuboid(*number_list[1:])
                    print(c)
                    print('-' * 15)
                else:
                    raise InvalidData('Ujemne wartości!')
            else:
                raise InvalidData('Za dużo lub za mało wartości!')
        except ValueError:
            print('Dane nie są liczbami!')
            print('-' * 15)
        except InvalidData as err:
            print(err)
            print('-' * 15)

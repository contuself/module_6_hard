import math

class Figure:
    sides_count = 0
    def __init__(self, color, *sides, filled = True):
        self.__sides = list(sides)
        self.__color = self.__is_valid_color(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        r, g, b = color
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            return [r, g, b]
        else:
            return self.__color

    def set_color(self, r, g, b):
        self.__color = self.__is_valid_color((r, g, b))

    def __is_valid_sides(self, *sides):
        for i in sides:
            if len(sides) == self.sides_count and isinstance(i, int) and i > 0:
                return True
            else:
                return False


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.__raduis = radius / (2*math.pi)

    def get_square(self):
        return math.pi * (self.__raduis)**2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        p = sum(self.__sides) / 2
        return (p * (p - sef.__sides[0]) * (p - sef.__sides[1]) * (p - sef.__sides[2])) ** 0.5

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, *([sides] * 12))
        self.sides = sides

    def get_volume(self):
        return self.sides**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится

print(cube1.get_color())



# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(cube1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())



# Проверка периметра (круга), это и есть длина:

print(len(circle1))



# Проверка объёма (куба):

print(cube1.get_volume())
from math import sqrt
from abc import ABC, abstractmethod
from prettytable import PrettyTable

class ChooseLang():
    def __init__(self, lang):
        self.lang = lang

l = ChooseLang('en') # en or ru 

class Figure(ABC):
    def __init__(self):
        return 'Создание фигуры..'
    
    @abstractmethod
    def area(self):
        return 'Площадь: xxx'

    @abstractmethod
    def perimeter(self):
        return 'Периметр: xxx'


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.name = 'Треугольник'
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

class Circle(Figure):
    def __init__(self, r):
        self.name = 'Круг'
        self.r = r

    def area(self):
        return 3.14 * (self.r**2)

    def perimeter(self):
        return 2 * 3.14 * self.r

class Quadrilateral(Figure):
    def __init__(self, a, b, c, d):
        self.name = 'Четырехугольник'
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def area(self):
        p = (self.a + self.b + self.c + self.d) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c) * (p - self.d))

    def perimeter(self):
        return self.a + self.b + self.c + self.d


# Класс для создания точки
class Point():
    def __init__(self):
        pass

    def get_point(self, x, y) :
        self.x = x
        self.y = y
        data = [self.x, self.y] 
        return data 

    def show(self):
        return 'Координаты: x = {}, y = {}'.format(self.x, self.y)

# Класс для создания стороны
class Side(Point):
    def __init__(self):
        pass
    
    def get_side(self, xy1, xy2):
        self.x1, self.y1 = xy1[0], xy1[1]
        self.x2, self.y2 = xy2[0], xy2[1]
        side = abs(sqrt((self.y2 - self.y1)**2 + (self.x2 - self.x1)**2))
        return int(side)

p = Point()
s = Side()

if l.lang == 'ru':
    fig_amount = int(input('Сколько фигур вы хотите создать?: '))
elif l.lang == 'en':
    fig_amount = int(input('How many shapes do you want to create?: '))


fig_dict = {}
for i in range(fig_amount):
    if l.lang == 'ru':
        fig_type = input('Какой тип фигуры вам нужен?(возможные типы: треугольник, круг, четырехугольк) ').lower()
    elif l.lang == 'en':
        fig_type = input('What type of figure do you need? (possible types: triangle, circle, square) ').lower()
    if fig_type == 'треугольник' or fig_type == 'triangle':
        x_1 = int(input('х1: '))
        y_1 = int(input('y1: '))
        x_2 = int(input('х2: '))
        y_2 = int(input('y2: '))
        x_3 = int(input('х3: '))
        y_3 = int(input('y3: '))
        tri = Triangle(s.get_side(p.get_point(x_1, y_1), p.get_point(x_2, y_2)), s.get_side(p.get_point(x_2, y_2), p.get_point(x_3, y_3)), s.get_side(p.get_point(x_3, y_3)), p.get_point(x_1, y_1))
        key, value = tri.name, tri.area()
        fig_dict[key] = value
    elif fig_type == 'круг' or fig_type == 'circle':
        x_1 = int(input('х1: '))
        y_1 = int(input('y1: '))
        x_2 = int(input('х2: '))
        y_2 = int(input('y2: '))
        circ = Circle(s.get_side(p.get_point(x_1, y_1), p.get_point(x_2, y_2)))
        key, value = circ.name, circ.area()
        fig_dict[key] = value
    elif fig_type == 'четырехугольник' or fig_type == 'square':
        x_1 = int(input('х1: '))
        y_1 = int(input('y1: '))
        x_2 = int(input('х2: '))
        y_2 = int(input('y2: '))
        x_3 = int(input('х3: '))
        y_3 = int(input('y3: '))
        x_4 = int(input('х4: '))
        y_4 = int(input('y4: '))
        quadr = Quadrilateral(s.get_side(p.get_point(x_1, y_1), p.get_point(x_2, y_2)), s.get_side(p.get_point(x_2, y_2), p.get_point(x_3, y_3)), s.get_side(p.get_point(x_3, y_3)), p.get_point(x_4, y_4), s.get_side(p.get_point(x_4, y_4)), p.get_point(x_1, y_1))
        key, value = quadr.name, quadr.area()
        fig_dict[key] = value
        

fig_dict = dict(sorted(fig_dict.items(), reverse = True, key=lambda x: x[1]))

mytable = PrettyTable()
mytable.field_names = ["Имя фигуры", "Площадь фигуры"]

for i in fig_dict:
    mytable.add_row([i, fig_dict[i]])

print(mytable)
    

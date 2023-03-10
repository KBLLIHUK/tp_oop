import sys
from Color import *


class Figure:
    def __init__(self, type):
        self.type = type
        self.void = None

    def get_from_file(self, line):
        if self.type == 1:
            self.void = Circle()
            self.coord1 = line[1].split()
            self.coord2 = line[2]
            self.WhatColor = WhatColor(int(line[3]))
        if self.type == 2:
            self.void = Rectangle()
            self.coord1 = line[1].split()
            self.coord2 = line[2].split()
            self.WhatColor = WhatColor(int(line[3]))
        if self.type == 3:
            self.void = Triangle()
            self.coord1 = line[1].split()
            self.coord2 = line[2].split()
            self.coord3 = line[3].split()
            self.WhatColor = WhatColor(int(line[4]))

    def record_to_file(self, file):
        if self.type == 1:
            file.write(
                f"Круг центр ({self.coord1[0]} {self.coord1[1]}), радиус {self.coord2}, цвет ")
            if self.WhatColor == WhatColor.red:
                file.write(f"красный")
            elif self.WhatColor == WhatColor.orange:
                file.write(f"оранжевый")
            elif self.WhatColor == WhatColor.yellow:
                file.write(f"желтый")
            elif self.WhatColor == WhatColor.green:
                file.write(f"зеленый")
            elif self.WhatColor == WhatColor.cyan:
                file.write(f"голубой")
            elif self.WhatColor == WhatColor.blue:
                file.write(f"синий")
            else:
                file.write("фиолетовый")
            file.write('\n\n')
        if self.type == 2:
            file.write(
                f"Прямоугольник ({self.coord1[0]},{self.coord1[1]}) ({self.coord2[0]},{self.coord2[1]}), цвет ")
            if self.WhatColor == WhatColor.red:
                file.write(f"красный")
            elif self.WhatColor == WhatColor.orange:
                file.write(f"оранжевый")
            elif self.WhatColor == WhatColor.yellow:
                file.write(f"желтый")
            elif self.WhatColor == WhatColor.green:
                file.write(f"зеленый")
            elif self.WhatColor == WhatColor.cyan:
                file.write(f"голубой")
            elif self.WhatColor == WhatColor.blue:
                file.write(f"синий")
            else:
                file.write("фиолетовый")
            file.write('\n\n')
        if self.type == 3:
            file.write(
                f"Треугольник ({self.coord1[0]},{self.coord1[1]}) ({self.coord2[0]},{self.coord2[1]}) ({self.coord3[0]},{self.coord3[1]}), цвет ")
            if self.WhatColor == WhatColor.red:
                file.write(f"красный")
            elif self.WhatColor == WhatColor.orange:
                file.write(f"оранжевый")
            elif self.WhatColor == WhatColor.yellow:
                file.write(f"желтый")
            elif self.WhatColor == WhatColor.green:
                file.write(f"зеленый")
            elif self.WhatColor == WhatColor.cyan:
                file.write(f"голубой")
            elif self.WhatColor == WhatColor.blue:
                file.write(f"синий")
            else:
                file.write("фиолетовый")
            file.write('\n\n')


class Circle:
    def __init__(self):
        self.coord1 = []
        self.coord2 = ""
        self.WhatColor = None


class Rectangle:
    def __init__(self):
        self.coord1 = []
        self.coord2 = []
        self.WhatColor = None


class Triangle:
    def __init__(self):
        self.coord1 = []
        self.coord2 = []
        self.coord3 = []
        self.WhatColor = None

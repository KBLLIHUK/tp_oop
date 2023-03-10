import sys
from Color import *


class Figure:
    def __init__(self, type):
        self.type = type
        self.void = None

    def get_from_file(self, file):
        if self.type == 1:
            self.void = Circle()
            self.coord1 = file.readline().strip()
            self.coord2 = file.readline().strip()
            self.WhatColor = WhatColor(int(file.readline()))
        if self.type == 2:
            self.void = Rectangle()
            self.coord1 = file.readline().strip()
            self.coord11 = self.coord1.split()[0]
            self.coord1 = self.coord1.split()[1]
            self.coord2 = file.readline().strip()
            self.coord21 = self.coord2.split()[0]
            self.coord2 = self.coord2.split()[1]
            self.WhatColor = WhatColor(int(file.readline()))

    def record_to_file(self, file):
        if self.type == 1:
            file.write(f"Круг центр {self.coord1}, радиус {self.coord2}\n")
            if self.WhatColor == WhatColor.red:
                file.write(f"Красный")
            elif self.WhatColor == WhatColor.orange:
                file.write(f"Оранжевый")
            elif self.WhatColor == WhatColor.yellow:
                file.write(f"Желтый")
            elif self.WhatColor == WhatColor.green:
                file.write(f"Зеленый")
            elif self.WhatColor == WhatColor.cyan:
                file.write(f"Голубой")
            elif self.WhatColor == WhatColor.blue:
                file.write(f"Синий")
            else:
                file.write("Фиолетовый")
            file.write('\n\n')
        if self.type == 2:
            file.write(
                f"Прямоугольник [{self.coord11},{self.coord1}] [{self.coord21},{self.coord2}]\n")
            if self.WhatColor == WhatColor.red:
                file.write(f"Красный")
            elif self.WhatColor == WhatColor.orange:
                file.write(f"Оранжевый")
            elif self.WhatColor == WhatColor.yellow:
                file.write(f"Желтый")
            elif self.WhatColor == WhatColor.green:
                file.write(f"Зеленый")
            elif self.WhatColor == WhatColor.cyan:
                file.write(f"Голубой")
            elif self.WhatColor == WhatColor.blue:
                file.write(f"Синий")
            else:
                file.write("Фиолетовый")
            file.write('\n\n')


class Circle:
    def __init__(self):
        self.coord1 = ""
        self.coord2 = ""
        self.WhatColor = None


class Rectangle:
    def __init__(self):
        self.coord1 = ""
        self.coord11 = ""
        self.coord21 = ""
        self.coord2 = ""
        self.WhatColor = None
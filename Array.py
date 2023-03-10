from Figure import *


def triangle_test(line):
    coord = [0, 0, 0]
    for i in range(1, 4):
        coord[i - 1] = list(map(int, line[i].split()))
    opr1 = coord[0][0] * coord[1][1] + coord[0][1] * \
        coord[2][0] + coord[1][0] * coord[2][1]
    opr2 = coord[2][0] * coord[1][1] + coord[0][0] * \
        coord[2][1] + coord[0][1] * coord[1][0]
    if (opr1 - opr2) == 0:
        return
    else:
        return "Ok"


class Array:
    def __init__(self, maxSize):
        self.size = 0
        self.content = []
        self.maxSize = maxSize

    def append(self, element):
        if self.size < self.maxSize:
            self.size += 1
            self.content.append(element)
        else:
            print("Массив уже заполнен! Элемент не будет записан")

    def clear(self):
        self.size = 0
        self.data = []

    def fill(self, file):
        line = file.readline().strip().split(", ")
        while line[0] != '':
            type = line[0]
            if type == "3":
                if triangle_test(line) is None:
                    print("Неправильно заданы координаты треугольника")
                    line = file.readline().strip().split(", ")
                    continue
            # print(type)
            figure = Figure(int(type))
            figure.get_from_file(line)
            self.append(figure)
            line = file.readline().strip().split(", ")

    def record_to_file(self, file):
        file.write(f"Записано {self.size} фигуры\n\n")
        for i in range(self.size):
            self.content[i].record_to_file(file)

import sys
from Figure import *

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
        type = file.readline()
        while type != '' and type != '\n':
            figure = Figure(int(type))
            figure.get_from_file(file)
            self.append(figure)
            type = file.readline()

    def record_to_file(self, file):
        file.write(f"Записано {self.size} фигуры\n\n")
        for i in range(self.size):
            self.content[i].record_to_file(file)
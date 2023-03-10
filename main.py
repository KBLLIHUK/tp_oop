import sys
from Array import *


if len(sys.argv) != 3:
    print('\nФайлы ввода/вывода не выбраны! Будут использованы стандартные in.txt и out.txt\n')
    infile = 'in.txt'
    outfile = 'out.txt'
else:
    infile = sys.argv[1]
    outfile = sys.argv[2]

infile = open(infile, 'r', encoding="utf-8")
a = Array(15)
a.fill(infile)
print(f"В контейнер записано {a.size} фигуры\n")
infile.close()

outfile = open(outfile, 'w', encoding="utf-8")
a.record_to_file(outfile)
outfile.close()
a.clear()
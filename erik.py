import numpy as np

f = open("a_example.txt", "r")

line_list = f.readline().split()
B = int(line_list[0])
L = int(line_list[1])
D = int(line_list[2])

library_books = np.full((L,B), False, dtype=bool)

line_list = f.readline().split()
book_values = np.array([float(x) for x in line_list])

n_books = np.zeros(L)
n_days = np.zeros(L)
ship_rate = np.zeros(L)

for l in range(L):
    line_list = f.readline().split()
    n_books[l] = int(line_list[0])
    n_days[l] = int(line_list[1])
    ship_rate[l] = int(line_list[2])
    line_list = f.readline().split()
    for b in [int(x) for x in line_list]:
        library_books[l, b] = True

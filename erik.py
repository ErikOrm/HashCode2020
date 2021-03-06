import numpy as np
import math
# f = open("a_example.txt", "r")
# f = open("b_read_on.txt", "r")
# f = open("c_incunabula.txt", "r")
# f = open("d_tough_choices.txt", "r")
# f = open("e_so_many_books.txt", "r")

def load_data(name):
    f = open(name, "r")

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

    return (B, L, D, library_books, book_values, n_books, n_days, ship_rate)


def get_library_value(B, library_books, book_values, l, remaining_time, ship_rate, setup_time):
    remaining_books = np.sum(library_books[l,:])
    prod = np.multiply(library_books[l,:], book_values)
    remaining_books_to_ship = remaining_time*ship_rate
    books_sent = np.cumsum(library_books[l,:])
    end = np.searchsorted(books_sent, remaining_books_to_ship)

    return np.sum(prod[:end])/setup_time, np.sum(prod[:end]), math.ceil((remaining_books_to_ship-remaining_books)/ship_rate)


def get_library_books(B, library_books, book_values, l, remaining_time, ship_rate):
    remaining_books = np.sum(library_books[l,:])
    remaining_books_to_ship = remaining_time*ship_rate
    books_sent = np.cumsum(library_books[l,:])
    end = np.searchsorted(books_sent, remaining_books_to_ship)

    return [x for x in range(end) if library_books[l,x] == True]


def print_solution(filename, libraries, books):
    f = open(filename, "w")
    f.write("%i\n" % len(libraries))
    for i in range(len(libraries) - 1):
        f.write("%i %i\n" % (libraries[i], len(books[i])))
        f.write("%s \n" % " ".join(str(x) for x in books[i]))
    f.write("%i %i\n" % (libraries[len(libraries)-1], len(books[len(libraries)-1])))
    f.write("%s" % " ".join(str(x) for x in books[len(libraries)-1]))
    f.close()



if __name__ == "__main__":
    print(np.argwhere(np.ones(5)>0)[0])

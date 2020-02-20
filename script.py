import numpy as np
import random
from erik import load_data
from emilio import set_up



# f = open("a_example.txt", "r")
# f = open("b_read_on.txt", "r")
# f = open("c_incunabula.txt", "r")
# f = open("d_tough_choices.txt", "r")
# f = open("e_so_many_books.txt", "r")
file = "f_libraries_of_the_world.txt"

B, L, D, library_books, book_values, n_books, n_days, ship_rate = load_data(file)

sortindex,book_value,library_books, gobackindex = set_up(book_values, library_books)

import numpy as np
import random
from erik import load_data, get_library_value
from emilio import set_up



# f = open("a_example.txt", "r")
# f = open("b_read_on.txt", "r")
# f = open("c_incunabula.txt", "r")
# f = open("d_tough_choices.txt", "r")
# f = open("e_so_many_books.txt", "r")
file = "f_libraries_of_the_world.txt"

    sortindex,book_values,library_books, gobackindex = set_up(book_values, library_books)
    #print(file)
    #print("Books:", B, "Libraries:", L, "Days:", D)
    #print("Largest bookvalues", book_values[0:5])
    #print("Smallest bookvalues", book_values[-5:])
    #print("Largest/Smallest setupdays", np.max(n_days), np.min(n_days))

    used_libary = np.zeros(L, dtype=np.bool)

    t = 0
    while t < D:
        scores = [get_library_value(B, library_books, lib_id, t-D, ship_rate)[0] if not used_libary[lib_id] else -1000 for lib_id in range(L)]
        np.argmax(scores)

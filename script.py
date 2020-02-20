import numpy as np
import random
from erik import load_data, get_library_value, get_library_books
from emilio import set_up


'''
a_example.txt
Books: 6 Libraries: 2 Days: 7
Largest bookvalues [6. 5. 4. 3. 2.]
Smallest bookvalues [5. 4. 3. 2. 1.]
Largest/Smallest setupdays 3.0 2.0
b_read_on.txt
Books: 100000 Libraries: 100 Days: 1000
Largest bookvalues [100. 100. 100. 100. 100.]
Smallest bookvalues [100. 100. 100. 100. 100.]
Largest/Smallest setupdays 20.0 1.0
c_incunabula.txt
Books: 100000 Libraries: 10000 Days: 100000
Largest bookvalues [600. 600. 600. 600. 600.]
Smallest bookvalues [1. 1. 1. 1. 1.]
Largest/Smallest setupdays 1000.0 10.0
d_tough_choices.txt
Books: 78600 Libraries: 30000 Days: 30001
Largest bookvalues [65. 65. 65. 65. 65.]
Smallest bookvalues [65. 65. 65. 65. 65.]
Largest/Smallest setupdays 2.0 2.0
e_so_many_books.txt
Books: 100000 Libraries: 1000 Days: 200
Largest bookvalues [250. 250. 250. 250. 250.]
Smallest bookvalues [1. 1. 1. 1. 1.]
Largest/Smallest setupdays 10.0 1.0
'''
files = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt"]

for file in files:
# f = open("a_example.txt", "r")
    B, L, D, library_books, book_values, n_books, n_days, ship_rate = load_data(file)

    sortindex,book_values,library_books, gobackindex = set_up(book_values, library_books)
    #print(file)
    #print("Books:", B, "Libraries:", L, "Days:", D)
    #print("Largest bookvalues", book_values[0:5])
    #print("Smallest bookvalues", book_values[-5:])
    #print("Largest/Smallest setupdays", np.max(n_days), np.min(n_days))

    used_libary = np.zeros(L, dtype=np.bool)

    t = 0
    while t < D:
        scores = np.array([list(get_library_value(B, library_books, book_values, lib_id, t-D, ship_rate, n_days[lib_id])) if not used_libary[lib_id] else (-1000,-1000) for lib_id in range(L)])
        print(scores.shape)
        new_library = np.lexsort(scores[:,1], scores[:,0])[0] #Check descending
        used_libary[new_library] = True
        t += n_days[new_library]
        used_books = get_library_books(B, library_books, book_values, new_library, t-D, ship_rate[new_library])
        for book in used_books:
            library_books[:,book] = False

        #Print out books to file



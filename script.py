import numpy as np
import random
from erik import load_data, get_library_value, get_library_books, print_solution
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
#files = ["a_example.txt"]


for file in files:
    print(file)
# f = open("a_example.txt", "r")
    B, L, D, lib, book, n_books, n_days, ship_rate = load_data(file)
    sortindex,book_values,library_books, gobackindex = set_up(book, lib)

    #print(file)
    #print("Books:", B, "Libraries:", L, "Days:", D)
    #print("Largest bookvalues", book_values[0:5])
    #print("Smallest bookvalues", book_values[-5:])
    #print("Largest/Smallest setupdays", np.max(n_days), np.min(n_days))

    used_library = np.zeros(L, dtype=np.bool)

    t = 0
    library_order = []
    book_order = []
    score = 0
    while t < D:
        print(t, "/", D)
        if L > 150:
            libindx = np.random.choice([i for i,x in enumerate(used_library) if not x],100, replace=False)
        else:
            libindx = [i for i, x in enumerate(used_library) if not x]

        scores = np.array([list(get_library_value(B, library_books, book_values, lib_id, D-t, ship_rate[lib_id], n_days[lib_id])) for lib_id in libindx])
        if len(scores) == 0:
            break
        new_library_idx = np.lexsort((scores[:,2], -1*scores[:,1]))[0]
        new_library = libindx[new_library_idx]
        used_library[new_library] = True
        t += n_days[new_library]
        used_books = get_library_books(B, library_books, book_values, new_library, D-t, ship_rate[new_library])
        for book in used_books:
            library_books[:,book] = False
        if len(used_books) == 0:
            break
        library_order.append(new_library)
        book_order.append(sortindex[used_books])

        score += scores[new_library_idx, 0]

    print_solution(file.split("_")[0] +"_"+ str(int(score)) + ".txt", library_order, book_order)




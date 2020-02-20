import numpy as np

def set_up(book_value, library_books):
    # library_books  = Libraries x Books
    sortindex = np.argsort(-1*book_value)
    gobackindex = np.argsort(sortindex)
    return sortindex,book_value[sortindex],library_books[:, sortindex], gobackindex


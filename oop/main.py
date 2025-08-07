from book_class import Book

def main():
    # create book instance
    book = Book("Atomic bomb", "Charles Oduks", 2025)
    
    # Usage of __str__ mthd
    print(book)
    # Usage of __repr__
    print(repr(book))
    # del a book instance
    del book
if __name__ == "__main__":
    main()

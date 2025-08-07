class Book:
    total_books = 0

    def __init__(self):
        
        Book.total_books += 1
    
    @classmethod
    def display_total_books(cls):
        return f"Total books in the Library is: {cls.total_books}"


book = Book()
book1 = Book()

print(Book.display_total_books())
print(book.display_total_books())

class Alla:
    count = 0

    def __init__(self):
        Alla.count += 1

    @classmethod
    def how_many(cls):
        return cls.count

    @staticmethod
    def greet():
        return "Hello from A"

a = Alla()
b = Alla()
print("\n-----Second Example-----")
print(b.how_many()) #class mthd
print(b.greet()) #static mthd


# ANOTHER TASK
print("\n------ANother TasK --------\n")

class Person:
    child_age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        

    def __repr__(self):
        
        return f"Person(name='{self.name}', age={self.age})"

    @classmethod
    def create_child(cls, name):
        
        return cls(name, cls.child_age)
    
    @staticmethod
    def how_many_children():
        return "child must be under 3 years old"
    
# usage
child = Person("Bobby", 8)
print(child.name)
print(child.age)
child1 = Person.create_child("Bobby Jnr")
print(child1.age)
print(Person.how_many_children())
print(Person.create_child("Joy"))
# Output: Person(name='Joy', age=0)

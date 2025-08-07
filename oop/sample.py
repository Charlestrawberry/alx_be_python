class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    def __del__(self):
        print(f"Goodbye {self.name}, your object is being deleted")
    
    def __str__(self):
        return (f"Person: {self.name}, Age: {self.age}")
    

person1 = Person("Joy", 37)
print(person1)


class Book:
    def __init__(self, title, author, pages):
        self.title = title  
        self.author = author  
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def read(self):
        print(f"Recommending {self.title} of {self.author}'s book")

book1 = Book("Atomic Habitat", "Charles Oduks", 298)
print(book1)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
    def make_sound(self):
        print(f"{self.name} says he can make sound")

class Dog(Animal): #Inheritance
    def bark(self):
        print(f"{self.name} says: Whoof Whoof")
    
    def make_sound(self):
        print(f"{self.name} is barking woo woo")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} says meow meow")

class Snake(Dog, Cat): #Multiple and Multilevel inheritance
    def make_sound(self):
        # return super().make_sound()
        print(f"{self.name} is Hissing")


snake1 = Snake("Anaconda")
snake1.bark()
snake1.make_sound()
animalia = Animal("Panther leo")
dog = Dog("Busky")
cat = Cat("Simbi")
animalia.eat()
animalia.sleep()



print("\n---\n")

dog = Dog("Busky")
dog.eat()
dog.bark()


phylum = [animalia, dog, cat]

for species in phylum:
    species.make_sound()


class Duck:
    def quack(self):
        return "Duck quacks"
class Person:
    def quack(self):
        return "Person imitates duck"

def making_sound(obj):
    return obj.quack()

duc = Duck()
per = Person()

print(making_sound(duc))
print(making_sound(per))
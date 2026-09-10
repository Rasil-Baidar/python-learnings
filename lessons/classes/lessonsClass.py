# This is a lesson on classes in Python

class Person:
    #  __init__ is the constructore that runs automatically when an object is created
    # self is the reference to the current object
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    
    def __str__(self)->str:
        return f"Person(name={self.name}, age={self.age})"

    def get_introduction(self)->str:
        return f"Hello, my name is {self.name} and I am {self.age} years old"
    # @property is a decorator that allows the method to be called without parentheses
    @property
    def speak(self)->str:
        return "Hello, I am speaking"

class BankAccount(Person):
    pass



def lesson_class():
    print("Class Lesson")
    print("--------------------------------\n")
    person = Person("John", 20)
    print(person.get_introduction())
    print("--------------------------------\n")
    print(person.speak)
    print("--------------------------------\n")
    print(person)
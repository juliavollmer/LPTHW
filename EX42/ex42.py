## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ##person has-a name
        self.name = name

        ## person has-a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ##Employee has-a name
        super(Employee, self).__init__(name)
        ##employee has-a salary
        self.salary = salary

## fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

##frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

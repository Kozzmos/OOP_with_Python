# In Python, we create an object using the "class" keyword. Inside the class,
# we define the attributes and methods that the object will have.
# Classes can be thought of as blueprints or prototypes for objects in the real world.

class Vehicle:
    # Attributes
    door_number = 0
    brand = ""
    model = ""
    engine_size = ""
    torque = 0

# Below, we create an instance of the Vehicle class.
# In software development, this process is called instantiation.
# The created instance is named 'x', and now 'x' has all the attributes of the Vehicle class.

# x = Vehicle()
# x.brand = "Mercedes"
# x.model = "C"
# x.engine_size = 5
# x.torque = 6
#
# print(f"Brand: {x.brand}")

# We can now create as many instances of the Vehicle class as we need,
# just like we can use the built-in list object as many times as we want with custom objects.

class Char:
    str = 0
    dex = 0
    cons = 0
    int = 0
    wis = 0
    char = 0

cs = Char()
cs.str = 3
cs.dex = 5
cs.cons = 6
cs.int = 4
cs.wis = 5
cs.char = 9

# When creating an instance, we used the class name like a function.
# This called the built-in __init__() method, which initializes the class.
# The __init__() method prepares the class for use and allocates it in the heap area of the memory.

class Boxer:
    # Class attribute
    alias = ""

    def __init__(self, firstname, lastname, age):
        # The following attributes are called object attributes
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        # 'self' represents the class itself

boxer1 = Boxer(firstname="Mike", lastname="Tyson", age=75)
print(dir(Boxer))
print(dir(boxer1))
boxer2 = Boxer(firstname="Mike", lastname="Tyson", age=45)
print(dir(boxer2))

class Circle:
    pi = 3.14

    def __init__(self, r):
        self.radius = r

    def calculate_area(self):
        return self.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * self.pi * self.radius

radius = float(input("Enter radius: "))
circle = Circle(radius)
print(f"Perimeter: {circle.calculate_perimeter()}")
print(f"Area: {circle.calculate_area()}")

class Department:
    department_name = "Software"
    employee_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Department.employee_count += 1
        self.show_information()
        self.show_employee_count()

    def show_information(self):
        print(self.name)
        print(self.age)
        print(self.department_name)

    def show_employee_count(self):
        print(self.employee_count)

employee1 = Department(name="Akif", age=19)
employee2 = Department(name="Akif", age=120)
employee3 = Department(name="Akif", age=14)

class SoftwareDeveloper:
    known_languages = ""

    def __init__(self, name, surname):
        self.firstname = name
        self.lastname = surname
        self.show_info()
        self.add_new_language()
        self.show_info()

    def show_info(self):
        print(f"Name: {self.firstname}\n"
              f"Lastname: {self.lastname}\n"
              f"{self.known_languages}\n")

    def add_new_language(self):
        new_langs = input("Write the languages you want to add: ").split(" ")
        self.known_languages += " ".join(new_langs) + " "

developer = SoftwareDeveloper("Akif", "Ertugrul")

from random import choice

class Char:
    def __init__(self, hp, armour, weapon, level, role, race, name):
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.level = level
        self.role = role
        self.race = race
        self.name = name

    def attack(self):
        return self.level * self.weapon

    def defend(self):
        return self.level * self.armour

    def dodge(self):
        print("Player has dodged")

def main():
    c1 = Char(100, 1, 100, 100, "Hero", "Turk", "Kara Murat")
    c2 = Char(100, 100, 20, 50, "Villain", "Byzantine", "Hain Kostok")

    while True:
        bot_actions = [c2.attack(), c2.defend(), c2.dodge()]
        bot_action = choice(bot_actions)
        c1_action = input("Type Action: ").lower()

        match c1_action:
            case "attack":
                pass
            case "defend":
                pass
            case "dodge":
                pass

main()

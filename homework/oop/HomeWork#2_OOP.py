
# TASK1

class Animals:
    def eat(self):
        print("Has to eat")

    def sleep(self):
        print("Ohhhh, i'm very tired, it's time to sleep")

animal = Animals()

class Animal1(Animals):
    def __init__(self, type, sound, speed):
        self.type = type
        self.sound = sound
        self.speed = speed

    def get_animal_info(self):
        return print(f"Animal 1 type: {self.type}. Animal's 1 sound: {self.sound}. Speed avarange: {self.speed} km/h")

    def hunt(self):
        print(f"{self.type} hunt on other animals.")

animal1 = Animal1("Tiger", "arrrrrrrrr", 75)

# animal1.get_animal_info()
# animal1.hunt()
# animal1.eat()
# animal1.sleep()

class Animal2(Animals):
    def __init__(self, type, sound, speed):
        self.type = type
        self.sound = sound
        self.speed = speed

    def get_animal_info(self):
        return print(f"Animal 2 type: {self.type}. Animal's 2 sound: {self.sound}. Speed avarange: {self.speed} km/h")

    def hunt(self):
        print(f"{self.type} is a tiger's friend.")

animal2 = Animal2("Lion", "rrrraaaarrrrr", 90)


# animal2.get_animal_info()
# animal2.hunt()
# animal2.eat()
# animal2.sleep()


class Animal3(Animals):
    def __init__(self, type, sound, speed):
        self.type = type
        self.sound = sound
        self.speed = speed

    def get_animal_info(self):
        return print(f"Animal 3 type: {self.type}. Animal's 3 sound: {self.sound}. Speed avarange: {self.speed} km/h")

    def making_friends(self):
        print(f"{self.type} wants to make a friend")

animal3 = Animal3("Wolf", "oouuuuuuuuuuu", 65)
#
# animal3.get_animal_info()
# animal3.making_friends()
# animal3.eat()
# animal3.sleep()


class Animal4(Animals):
    def __init__(self, type, sound, speed):
        self.type = type
        self.sound = sound
        self.speed = speed

    def get_animal_info(self):
        return print(f"Animal 4 type: {self.type}. Animal's 4 sound: {self.sound}. Speed avarange: {self.speed} km/h")

    def inspection_of_the_territory(self):
        print(f"{self.type} is an inspector")

animal4 = Animal4("Giraffe", "Khmmm, what is going on???", 30)
#
# animal4.get_animal_info()
# animal4.inspection_of_the_territory()
# animal4.eat()
# animal4.sleep()
#
class Animal5(Animals):
    def __init__(self, type, sound, speed):
        self.type = type
        self.sound = sound
        self.speed = speed

    def get_animal_info(self):
        return print(f"Animal 5 type: {self.type}. Animal's 5 sound: {self.sound}. Speed avarange: {self.speed} km/h")

    def character(self):
        print(f"{self.type} is very noisy")

animal5 = Animal5("Crocodile", "clac clac clac", 20)
#
# animal5.get_animal_info()
# animal5.character()
# animal5.eat()
# animal5.sleep()

# print(isinstance(animal1, Animals))
# print(isinstance(animal2, Animals))
# print(isinstance(animal3, Animals))
# print(isinstance(animal4, Animals))
# print(isinstance(animal5, Animals))

#TASK2

class Human:

    def __init__(self, type, age, iq):
        self.type = type
        self.age = age
        self.iq = iq


    def sleep(self):
        print(f" {self.type} Has to sleep")

    def eat(self):
        print(f"{self.type} Has to eat")

    def work(self):
        print(f"{self.type}Has to work")

    def study(self):
        print(f"{self.type} Has to study")


human = Human("boy", 17, 170)

class Centaur(Animal1, Human):

    def __init__(self, type, speed, gun, move):
        self.type = type
        self.speed = speed
        self.gun = gun
        self.move = move

    def action(self):
        print(f"{self.type} can use {self.gun} and {self.move}")


centaur = Centaur("Centaur", 70, 'pistol','jump')
#
# centaur.hunt()
# centaur.action()
# centaur.eat()

#task3

class Person:
    def __init__(self):
        arm_1 = Arm('left')
        arm_2 = Arm('right')
        self.arms = [arm_1, arm_2]

class Arm:
    def __init__(self, quantity):
        self.quantity = quantity

    def __call__(self):
        return print(f"Person has {self.quantity} arms")

arm = Arm(2)


# arm()
# person = Person()



class CellPhone():
    def __init__(self, screen):
        self.screen = screen



class Screen(CellPhone):
    def __init__(self):
        pass

# task 4


class Stranger:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Name and last name:\t{self.name} {self.last_name} \nPhone_number:\t{self.phone_number} " \
               f"\nBirthday\t{self.birthday} \nAge:\t{self.age} \nSex:\t{self.sex} \nAddress:\t" \
               f"{self.address} \nEmail:\t{self.email}"


stranger = Stranger('Dan', 'Balan', '3123445321', 'strocova street', 'jgtgij@gmail.com', '08.12.2001', '29', 'man')
#
# print(stranger)

from abc import  ABC, abstractmethod
class Laptop:

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webCam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamics(self):
        pass

class HPLaptop:

    def __init__(self, model):
        self.model = model

    def screen(self):
        print(f'{self.model} has a big screen')

    def keyboard(self):
        print(f'{self.model} has very quiet keyboard')

    def touchpad(self):
         print(f'{self.model} has convenient touchpad ')

    def webcam(self):
         print(f'{self.model} has a camera of 150 pixels')

    def ports(self):
         print(f'{self.model} has 5 ports')

    def dynamics(self):
         print(f'{self.model} has very loud dynamics')
#
# hplaptop = HPLaptop('Asus')
# hplaptop.screen()
# hplaptop.keyboard()
# hplaptop.touchpad()
# hplaptop.webcam()
# hplaptop.ports()
# hplaptop.dynamics()











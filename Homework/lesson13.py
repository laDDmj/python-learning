#Task 1

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstname}{self.lastname} and I’m {self.age} years old.')

person1 = Person('Carl', 'Johnson', '26')
person1.talk()


#Task 2

class Dog:
    age_factor = 7
    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * self.age_factor
dog1 = Dog(7)
print(f'Dog age in human equivalent is: {dog1.human_age()}')


# Task 3

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current = 0

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def next_channel(self):
        self.current = (self.current + 1)
        return self.channels[self.current]

    def previous_channel(self):
        self.current = (self.current - 1)
        return self.channels[self.current]

    def current_channel(self):
        return self.channels[self.current]

    def turn_channel(self, N):
        if 1<=N<=3:
            self.current = N - 1
            return self.channels[self.current]
        else:
            return (f'Error! Just these 3 channels: {self.channels}')

    def is_exist(self, channel):
        if channel  in self.channels:
            return 'Yes'
        else:
            return 'No'


controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"







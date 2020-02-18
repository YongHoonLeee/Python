class Person(object):
    def __init__(self, age =1):
        self.age = age
    def drive(self):
        if self.age>=18:
            print('OK')
        else:
            raise Exception('No drive!')

class Baby(Person):
    def __init__(self,age =1):
        if age <18:
            super().__init__(age)
        else:
            raise ValueError
class Adult(Person):
    def __init__(self,age =18):
        if age >=18:
            super().__init__(age)
        else:
            raise ValueError

baby = Baby()
adult = Adult()

class Car(object):
    def ride(self,Person):
        Person.drive()
    
car = Car()
#car.ride(baby)
car.ride(adult)

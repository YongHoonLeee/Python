class Person(object):
    def __init__(self,name): # 생성자
        self.name = name
        print('First')
    def say_hello(self):
        print('Hi , I\'m {}. hello~ ;)'.format(self.name))

    def __del__(self):         # 소멸자
        print('good bye My name is {}.'.format(self.name))

yonghoon = Person('YongHoon')
yonghoon.say_hello()
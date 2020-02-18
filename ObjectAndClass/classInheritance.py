class Car(object):
    def __init__(self,name):
        self.name = name
        print(self.name)
    def run(self):
        print('run')
    pass

class Tesla(Car): # 상속됨.
   def __init__(self, name):
       super.__init__(name)
           
    def auto_run(self):
        print('auto_run')
    pass

simple_car = Car('simple_Car')
auto_car = Tesla('auto_Car')
print("###########")
auto_car.auto_run()
auto_car.run()
simple_car.run()
class Car(object):
    def drive(self):
        print('부릉부릉')
    

class robot(object):
    def run(self):
        print('헛둘 헛둘 ㅋㅋㅋㅋ')
    

class car_robot(Car,robot):
    def driveAndRun(self):
        print('붓둘 릉둘 붓둘 릉둘')
    

silver = car_robot()

silver.driveAndRun()
silver.run()
silver.drive()
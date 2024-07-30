#Types of variables
class car:
    wheel=4     #class variable
    
    def __init__(self):
        self.mil= 10            #instance variable
        self.com= 'BMW'

c1=car()
c2=car()

c1.mil=8

car.wheel=5

print(c1.com, c1.mil,car.wheel)
print(c2.com, c2.mil,car.wheel)


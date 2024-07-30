class computer:
    
    def __init__(self):
        self.name='Manju'
        self.age=21
    
    def compare(self,other):
        if self.age== other.age:
            return True
        else:
            return False
        
c1=computer()  #creating an object
c2 =computer()

c2.age=22
if c1.compare(c2):
    print('They are same')
else:
    print('They are different')

print(c2.name)
print(c2.age)



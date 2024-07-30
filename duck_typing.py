# The class of an object is less important than the method it defines.
# Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute.
# In python, we have dynamic typing, we didn't need to worry about the data type of the variable.
class duck:
    def swim(self):
        print('I am a duck and I can swim')
    def speaks(self):
        print('Quack Quack')
    
class dog:
    def swim(self):
        print('I am a dog and I can swim')
    def speaks(self):
        print("woof woof")
    
def display(obj):
    obj.swim()
    obj.speaks()
    print('Information Displayed')
    
d=duck()
dog=dog()
display(dog)

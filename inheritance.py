#inheritance
class A:
    def feature1(self):
        print('feature-1 is working')
        
    def feature2(self):
        print('feature-2 is working')

class B(A): #b is inheriting all properties of class a (B is child class and A is parent class)
     def feature3(self):
        print('feature-3 is working')
    
     def feature4(self):
        print('feature-4 is working')
        

a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature1()
b1.feature4()

# In Inheritance, we have
# single-level Inheritance =B(A)
# Multi-level Inheritance=C(B)
# Multiple Inheritance=Z(X,Y)


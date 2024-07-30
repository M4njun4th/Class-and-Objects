class A:
    
    def __init__(self):
        print('in A init')
        
    def feature1(self):
        print('feature-1 is working')
        
    def feature2(self):
        print('feature-2 is working')

class B: 
    
    def __init__(self):
        print('in B init')
        
    def feature3(self):
        print('feature-3 is working')
    
    def feature4(self):
        print('feature-4 is working')
        
class C(A,B): 
    
    def __init__(self):
        super().__init__()  #It only print A init bcoz it follows Method Resolution Order(MRO)
                            #whenever we have multiple inheritance it starts from left to right
        print('in C init')
        
    def feature3(self):
        print('feature-5 is working')
    
    def feature4(self):
        print('feature-6 is working')
        
c1=C()



    
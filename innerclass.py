#class inside a class
class student:  #outer class
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()   # creating laptop object
    
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
        
        
    class laptop:   #inner class
        def __init__(self):
            self.brand='HP'
            self.ram= 8
        
        def show(self):
            print(self.brand, self.ram)
          
            
        
        
s1=student('manju', 21)
s2=student('ravi',24)

s1.show()


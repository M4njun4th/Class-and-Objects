#Types of Methods
class student:
    school ='GHS'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def avg(self):
        return (self.m1 +self.m2+ self.m3)/3
    
    @classmethod      #decorators
    def getschool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print('This is student class')
        
    
    
s1=student(4,8,12)
s2=student(5,10,15)

print(s1.avg())
print(student.getschool())
student.info()



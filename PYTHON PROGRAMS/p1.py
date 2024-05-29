# class Person:
#      def __init__(self,fname,lname): 
#         self.firstname=fname 
#         self.lastname=lname 
# class Person: 
#     def __init__(self,fname,lname): 
#         self.firstname=fname 
#         self.lastname=lname
# def printname(self): 
#     print(self.firstname,self.lastname) 
# p1=Person('Ayush','Shah') 
# p1.printname() 
class Person: 
    def __init__(self,fname,lname): 
        self.firstname=fname 
        self.lastname=lname 
    def printname(self): 
        print(self.firstname,self.lastname) 
p1=Person('Ayush','Shah') 
print("Modification") 
 
p1.printname() 
print("after Changing:") 
# del(p1)
p1.firstname=('Aaryan') 
p1.printname() 

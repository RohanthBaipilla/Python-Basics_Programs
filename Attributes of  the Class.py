#Attributes of a class
''' 1. getattr() -->Accessing the Class Attributes
    2. setattr() -->Modifying the Class Attributes
    3. hasattr() -->Checking the Attributes of the Class
                        i. if it has --> return True
                        ii.else   -->return False
    4. delattr() -->Deleting the Attributes of the Class '''

class Person:
    name="Rohanth"
    age=19
    address="Kothapeta"
j=Person()
print(getattr(j,'name'))
setattr(j,'age',20)#After Setattr we have to use getattr function to get updated information
print(getattr(j,'age'))
print(hasattr(j,'address'))
delattr(j,'address')
print(getattr(j,'address')) #The Error will be Raised when we access the deleted Attributes

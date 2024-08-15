#scenarios where various object within a class have unique attributes or properties 
#creation of a class
class ballot:
    #initiate the__init__method or constructor to initialize the objects properties or attributes
    def __init__(self,elem):      #first method that has the first attribute of the object
        self.first_key = elem
        
    def pull(self,elem=2):
        self.second_key=elem

object_1=ballot(2)# object1_1 has two properties(first_key and second_key)
object_1.pull(1) 
object_2=ballot(3)# object_2 has one attribute(first_key)
object_3=ballot(4)
object_3. third =5 #object_3 has two attributes also but the second attribute was not defined by a method and its pemissible
# the attributes being (first_key and third)

print(object_1.__dict__)
print(object_2.__dict__)
print(object_3.__dict__)
        
        
    
class sample:
    gamma=0 #class variable
    def __init__(self):
        self.alpha=1
        self.__delta=2 #private instance variable that can only called within the class or accessed externally when mangled 
        
obj=sample()
obj.beta=3 #an object intstance that is accessed only by the(obj)object.
get=sample()
print(obj.__dict__)#gamma is not included because it is a class variable.
print(get.__dict__)
print(hasattr(sample,"gamma"))
print(hasattr(obj,"beta"))
print(hasattr(get,"beta"))
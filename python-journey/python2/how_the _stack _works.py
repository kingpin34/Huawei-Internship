class stack:
    def __init__(self):
        self.__stk=[]
        
    def push(self,val):
        self.__stk.append(val)
        
    def pop(self):
        val=self.__stk[-1]
        del self.__stk[-1]
        return val
    
class countingstack(stack):
    def __init__(self):
        stack.__init__(self)
        self.__counter=0
     
    def get_counter(self):
        return self.__counter
     
    # def push(self, val):
    #     self.__counter+=1
    #   return  stack.push(self,val)
        
    def pop(self):
       self.__counter +=1
       return stack.pop(self)
   
stk=countingstack()
   
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())


        
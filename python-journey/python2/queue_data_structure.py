#The Queue data structure makes use of the FIFO (First in first out model)
class QueError(RuntimeError): #Class is derived from RuntimeError exception even tho its an empty class
    pass

class Queue():
    def __init__(self):
        self.__queue_list=[]
        
    def put(self,val):
        self.__queue_list.append(val)
        
    def get(self):
        if not self.__queue_list:
              raise QueError
        val=self.__queue_list[0]
        del self.__queue_list[0]
        return val
       #or you could use self.__queue_list.pop(0)
    
que=Queue()
que.put(1)
que.put("Dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print ("Queue error")
    
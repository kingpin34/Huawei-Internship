#!/usr/bin/env python3

"module.py - an example of python module"
__counter=0

def sum1(My_list):
    global __counter
    __counter +=1
    the_sum=0
    for element in My_list:
        the_sum =+ element
    return the_sum
        
def prod1(My_list):
    global __counter
    __counter +=1
    prod=1
    for element in My_list:
        prod*=element
    return prod

if __name__ =="__main__":
     print("I prefer to be a module,but i can do the test for you")
     My_list=[i+1 for i in range(5)]
     print(sum1(My_list) == 15)
     print(prod1(My_list) ==120)
    #  print(My_list)
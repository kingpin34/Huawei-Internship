# blocks=int(input("Kindly enter the number of blocks:"))
# height=0
# blocks_used=0
# while blocks_used + height +1<= blocks:
#     height+=1
#     blocks_used+= height
# print("the height of your pyramid is:",height)    
print()
c0=int(input("Enter a non-negative or non-zero number"))
steps=0
if c0 > 0:
    while c0!=1:
        print(c0)
        c0=c0//2
    else:
        c0=3 * c0 + 1
        steps+=1
    print(c0)    
    print("steps=" ,steps)
else:    
    print("please enter a non-zero or non-negative number:")        
        
  

 


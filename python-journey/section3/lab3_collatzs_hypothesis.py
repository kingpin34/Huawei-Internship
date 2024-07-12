blocks=int(input("Kindly enter the number of blocks:"))
height=0
blocks_used=0
while blocks_used + height +1<= blocks:
    height+=1
    blocks_used+= height
print("the height of your pyramid is:",height)    
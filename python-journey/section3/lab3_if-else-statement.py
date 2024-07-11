income= float(input("Please enter your income:"))
if income < 85528:
    tax= 0.18 *income - 556.02
elif income > 85528:
    tax= 14839.02 + 0.32 *(income-85528)
if tax < 0:
    tax=0.0
print("The tax is",tax,"thalers")   
print()
year=(int(input("Enter the year number:")))  
if year < 1582:
    print("Not within the geogerian calendar")
else:    
    if year % 4 !=0:
        print("common year")
    elif year % 100 !=0:
        print("Leap year")
    elif year % 400 !=0:
        print("common year") 
    else:
        print("leap year")      


   
   
         
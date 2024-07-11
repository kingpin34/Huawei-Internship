income= float(input("Please enter your income:"))
if income < 85528:
    tax= 0.18 *income - 556.02
elif income > 85528:
    tax= 14839.02 + 0.32 (income-85528)
if tax < 0:
    tax=0.0
print("The tax is",tax,"thalers")        
         
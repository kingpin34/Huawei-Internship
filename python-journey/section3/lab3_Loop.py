# odd_number=0
# even_number=0
# number=int(input("Enter an odd number or even number:"))
# while number != 0:
#     if number% 2 ==1:
#         odd_number +=1
#     else:
#         even_number +=1
#     number=int(input("Enter another odd number or even number or press 0 to stop:"))
# print("The number of odd numbers are:" ,odd_number) 
# print("The number of even numbers are:",even_number)
       
print(
    """
      +============================+
      | Welcome to my game ,Muggle |
      | Enter an integer number    | 
      |                            | 
      | Guess what I've picked for |
      |  you                       |
      |  so,what is the secret     |
      | number?                    |
      +============================+
    """
)
secret_number=722
number=int(input("please enter your guessed number:"))
while number != secret_number:
    print("ha ha you are stuck in my loop")
    number=int(input("please enter your guessed number:"))
print(secret_number,"well done you are free now!!" )    
    
    
    

    

 
birth_date = input("Enter your date of birth in (YYYY-MM-DD) format:")#Accepts the date of birth of the user
if len(birth_date)!=10:
    print("Please enter a valid date of birth")#Validate the format of the birthdate by using the length of element
else:
    birth_date = birth_date.replace("-","")#removes the hyphen from the from the string content
    total = 0 #initializes the value of  the variable total to Zero
    for d in birth_date:#iteratre through the element in the string
        total+=int(d)# add the digits in the string(birthdate)converted to an integer to variable total
    while len(str(total))>1:
        new_total=0
        for d in str(total):
            new_total+=int(d)#reduces the values of totaal to a single digit
        total=new_total
               
print(total,"is the digit of life")

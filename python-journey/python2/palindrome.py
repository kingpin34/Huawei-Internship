Text=input("Enter  your text:")
Text=Text.replace(" ","")
if len(Text) > 1 and Text.upper() == Text[::-1].upper():
    print("Its a palindrome")
else:
    print("Its not a palindrome")
    
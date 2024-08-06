def improved_cipher(msg,shift): 
    # msg=input("Enter your text:") #accept the msg of the user
    # shift=int(input("Enter the number of shift from(1-25)")) #accept the number of shift 
    text=""
    if not shift in range(1,26):
        print("Enter a valid shift number from(1-25):") # validate the number of shift
    else:
        for char in msg:
            if char.isalpha():
                code=ord(char)+shift
                if char.islower():
                    first=ord("a")
                else:
                    first=ord("A")
                code-=first
                code%=26
                text+=chr(first+ code)
            else:
                text +=char   
    print(text)           
    
print(improved_cipher("The die cast" ,25))

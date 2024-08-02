IBAN=input("please enter your IBAN:")#user enters his or her IBAN 
IBAN=IBAN.replace(" ","")#we remove the spaces within the IBAN

if not IBAN.isalnum():
    print("You have entered invalid characters for your IBAN")
elif len(IBAN) < 15:
    print("Your IBAN is too short")
elif len(IBAN)> 31:
            print("your IBAN  is too long") #check if the IBAN has the required length
else:
    IBAN=(IBAN[4:] + IBAN[:4]).upper()
    IBAN2=[]#this variable is going to store the IBAN number after the letters has been changed to digits 
    for ch in IBAN:
        if ch.isdigit():
            IBAN2 += ch
        else:
            IBAN2+=str(10 + ord(ch)-ord("A"))
    IBAN=int(IBAN2)
    if IBAN % 97 == 1:
        print("The IBAN number your entered is valid!!!")
        
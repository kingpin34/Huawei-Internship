# text = input("please enter your Text message:")
# cipher=""
# for char in text:
#     if not char.isalpha():
#         continue
#     char=char.upper()
#     code=ord(char) + 1
#     if code > ord("Z"):
#         code=ord("A")
#     cipher+=chr(code) 
# print(cipher)


#cipher with three postional place to  the left for En and to the right for deciphering in a function

def Ceasar_cipher(text):
    cipher=""
    for ch in text:
        if ch.isalpha():
            ch=ch.upper()
            code=ord(ch) + 23
            if code > ord("Z"):
                code-=26
            cipher +=chr(code) 
        else:
            cipher+=ch       
    return cipher

print(Ceasar_cipher("the"))


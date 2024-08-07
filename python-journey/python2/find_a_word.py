word=input("Please type your word:").upper()
strn=input("enter the second group of characters").upper()
start=0
found=True
for ch in word:
    pos=strn.find(ch,start)
    if pos < 0:
        found=False
        break
    start= pos + 1
if found:
    print("yes")
else:
    print("No")
    
first_word=input("Enter the first word:")
second_word=input("Enter the second word:")#accept both words from user
first_word=first_word.replace(" ","")
second_word=second_word.replace(" ","")#removes all spaces within string before checking
#convert words to list
first_word,second_word=first_word.upper(),second_word.upper()

str_1=list(first_word)
str_2=list(second_word)
str_1=sorted(str_1)
str_2=sorted(str_2)
combo=str(str_1 + str_2)
print(combo)
if str_1 == str_2:
    print("It is an anagram")
else:
    print("It s not an anagram")

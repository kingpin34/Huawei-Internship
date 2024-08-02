def mysplit(strng):
    #check to see if the input is a string
    if strng=="":
        return []
    else:
        #create a new list to be returned
        my_list=[]
        # A variable initialized to an empty string so it could store each word in the string
        current_word=""
        #create a loop to move through or iterate through the string (ie. the typed sentence)the for loop would be ideal
        for ch in strng:
            if ch!=" ":#check if the character is a space
                current_word+=ch
            else:
                if current_word:
                    my_list.append(current_word)
                    current_word=""
    return(my_list)           
    
print(mysplit("To God be, The Glory"))


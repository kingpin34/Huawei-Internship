def read_int(prompt, min,max):
    
    while True:
        try:
            value=int(input(prompt))
        except ValueError:
            print("Error:Wrong input, please enter a valid input data type")
        except:
            print("oh sorry, something happened")
            if value < min or value >max:
                print("Error: the value you entered is not within the permitted range of {}...{}" .format(min,max))
            else:
                    break
    return value


v=read_int("Enter a value from -10 to 10:",-10,10)
print("The number is:",v)
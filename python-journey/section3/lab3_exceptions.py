try:
    value=int(input("please enter a valid natural number:"))
    print("The reciprocal of",value,"is",1/value)
except ValueError:
    print("you entered a wrong data")
except ZeroDivisionError:
    print("zero division is not allowed in our universe")
except:
    print("sorry something came up")    
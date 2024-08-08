from math import exp
ex=1
while True:
    try:
        print(exp(ex))
        ex*=2
    except OverflowError:
        print("the number is to big to be stored")
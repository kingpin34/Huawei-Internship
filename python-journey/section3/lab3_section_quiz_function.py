def my_book(first):
    print("Print #1",first)
    print("Print #2",second)
    first=[2,3]
    print("print #4",first)
    print("print #4",second)

second=[3,4]
my_book(second)
def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
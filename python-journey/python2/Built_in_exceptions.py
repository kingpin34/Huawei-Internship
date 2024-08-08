my_list=[1,2,3,4,5]# A list is created and assinged a series of of integers or non-zero numbers.
ix=0
do_it=True# 0 an True assigned to variables ix and do_it
while do_it:
    try:
        print(my_list[ix])
        ix+=1
    except IndexError:# handles exception as a result of an index that is not within the range of the list
        do_it=False
print("We are done")
# # accept input from the user
# Hour=int(input("please enter the hours (hours):"))
# min=int(input("Please enter the minutes (minutes):"))
# Dur=int(input("Please enter the duration (minutes):"))
# # find total of all minutes
# min = min + Dur
# # find the number of hours hidden in the minutes
# Hour= Hour + min // 60
# # ensuring minutes follows the range (0....59)
# min= min % 60
# Hour= Hour % 24
# print("your end time for this activity is ", Hour ,":" ,min, sep="")
x = int(input())
y = int(input())
 
x = x / y
y = y / x
 
print(y)
# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
 
 
# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b
 
 
# def heron(a,b,c):
#     s=(a+b+c)/2
#     return (s*(s-a)*(s-b)*(s-c))**0.5

# def Area_of_triangle(a,b,c):
#     if not Area_of_triangle(a,b,c):
#         return None
#     return heron(a,b,c)

# print(Area_of_triangle(3,4,5))


# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
 
# #     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product
 
 
# for n in range(1, 6): # testing
#     print(n, factorial_function(n))
 
def fib(n):
    if n < 0:
        return None
    if n < 3:
        return 1
    
    elem_1=elem_2 = 1
    next_fib_num=0
    for i in range(3, n + 1):
        next_fib_num=elem_1 + elem_2
        elem_1,elem_2= elem_2,next_fib_num
    return next_fib_num

for n in range (1,6):
    print(n,fib(n))    
        
        
 
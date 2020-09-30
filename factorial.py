# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f*i
#     return f
# result = fact(5)
#
# print(result)

# import sys
#
# sys.setrecursionlimit(2000)
#
# print(sys.getrecursionlimit())
#
# i=0
# def greet():
#     global i
#     i+=1
#     print("hello",i)
#     greet()
# greet()


#Recursion meaning function calling in itself

# Factorial function using regression

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
result = fact(5)
print(result)
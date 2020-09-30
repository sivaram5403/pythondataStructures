# def greet():
#     print('hello welcome to python learning')
#     print('thank you')
# greet()
#
# def multi(x,y):
#     c = x*y
#     return c
# print(multi(8,6))
#
# def add_sub(x,y):
#     d = x+y
#     e = x-y
#     return d,e
# result1,result2 = add_sub(9,5)
# print(result1)
# print(result2)

# Variable length

# def sum(*b):
#     c=0
#     for i in b:
#         c=c+i
#     print(c)
# sum(2,4,6,78,8)

#keyword variable

# def person(name,**data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
#
# person('siva',age=27,city = "newyork" , mob = 7034624689)


lst = []

n =int(input("enter the length of array :"))

for i in range(n):
    x=int(input("enter the element in list"))
    lst.append(x)
print(lst)

def count(lst):
    even =0
    odd =0
    for i in lst:
        if i%2 ==0:
            even+=1
        else:
            odd+=1
    return even,odd
even,odd = count(lst)
print('even : {} and odd : {} '.format(even,odd))


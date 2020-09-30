
#Reading a file
f = open('mydata','r')

# print(f.read())

# print(f.readline())

#Writing a file

# f1 = open('abc','w')
#
# f1.write("this is new file 1")

#appending
f1 = open('abc','a')

# f1.write("this is new file 2")

for data in f:
    f1.write(data)

#using for loop
# arr0 = [2,3,4,5,12,9,10]
#

pos = -1
def search(arr1,n):
    for i in range(len(arr1)):
        if arr1[i] == n:
            globals()['pos'] = i
            return True

# pos = -1
# def search(arr1,n):
#     i = 0
#     while i < len(arr1):
#         if arr1[i] == n:
#             globals()['pos'] = i
#             return True
#         i+=1
#     return False
arr1 = [2,3,4,5,12,9,10]
#
n= 9

if search(arr1,n):
    # print("found value at",pos+1)
    print("found value at ", pos+1)
else:
    print("value is not found")
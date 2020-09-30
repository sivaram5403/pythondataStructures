from functools import reduce

#filter function takes 2 arguments function and iterator and it is filter list of values based on function
nums = [2,36,4,3,7,4,9,10]
evens = list(filter(lambda n : n%2 == 0,nums))
print(evens)

double = list(map(lambda n : n*2,evens))
print(double)

sum = reduce(lambda a,b : a+b, double)

print(sum)


def topten():

    n = 1
    while n <=10:
        sq = n*n
        yield sq
        n+=1
t1 = topten()

for i in t1:
    print(i)
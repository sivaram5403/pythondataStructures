def fibonacci(n):
    a=0
    b=1
    if n>0:
        print("entered valid input")
        if n ==0:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(1,n):
                c=a+b
                a=b
                b=c
                print(c)
    else:
        print("entered invalid input")
fibonacci(3)

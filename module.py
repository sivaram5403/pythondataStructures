from decorators import add
def fun1():
    add()
    print("this is fun1")

def fun2():
    print("this is fun2")

def main():
    fun1()
    fun2()

main()
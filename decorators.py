# def sub(a,b):
# # #     print(a-b)
# # #
# # # def smartsub(func):
# # #     def inner(a,b):
# # #         if a<b:
# # #             a,b = b,a
# # #         return func(a,b)
# # #     return inner
# # # sub = smartsub(sub)
# # # sub(1,3)


def add():
    print("result of add", __name__)

def sub():
    print("result of sub")

def main():
    add()
    sub()

if __name__ == '__main__':
    main()


class A:

    def  __init__(self):
        print("class a init method")
    def feature1(self):
        print("feature 1 is working")

    def feature2(self):
        print("feature 2 is working ")


class B(A):

    def __init__(self):
        super().__init__()
        print("class b init method")
    def feature3(self):
        print("feature 3 is working")

    def feature4(self):
        print("feature 4 is working ")

# class C (A,B):
#     def feature5(self):
#         print("feature 5 is working")
#
#     def feature6(self):
#         print("feature 6 is working ")
# a1= A()
b1 = B()
b1.feature1()
# c1 = C()
# b1.feature1()
# c1.feature2()

class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name,self.rollno,self.lap)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand = "hp"
            self.ram = "8gb"

        def show(self):
            print(self.brand,self.ram)


s1 = student("sivaram",33)
s1.show()

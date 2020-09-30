class student:
    school = "Telusko"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def get_school(cls):
        return cls.school
    @staticmethod
    def info():
        print("this is static method")

c1 = student(12,45,12)
c2 = student(34,12,45)

print(c1.avg())
print(c2.avg())
print(student.get_school())
student.info()


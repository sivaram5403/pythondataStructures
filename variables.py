class car :
    wheels = 4
    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = car()
c2 = car()

car.wheels = 5
print(c1.mil,c1.com,c1.wheels)

print(c1.mil,c2.com,c2.wheels)
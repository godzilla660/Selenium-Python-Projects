class AreaRect:
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def calculate_Area(self):
        return self.l * self.h

area1 = AreaRect(8,5)
area2 = AreaRect(65,30)
print(area1.calculate_Area())
print(area2.calculate_Area())


try:
    print("Enter first number: ")
    x= int(input())
    print("Enter second number: ")
    y= int(input())

    result = (x/y)
    print(result)
except Exception as e:
    print(e)

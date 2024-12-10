class Rectangle:
    def __init__(self,length,breadth):
        self._length=length
        self._breadth=breadth
    def area(self):
        return self._length*self._breadth
    def __lt__(self,other):
        return self.area()<other.area()
print("Rectangle1:")
length1=int(input("Enter the length of rectangle1:"))
breadth1=int(input("Enter the breadth of rectangle1:"))
rect1=Rectangle(length1, breadth1)
print(f"The area of rectangle1 is:{rect1.area()}")
print("\nRectangle2")
length2=int(input("Enter the length of rectangle2:"))
breadth2=int(input("Enter the breadth of rectangle2:"))
rect2=Rectangle(length2, breadth2)
print(f"The area of rectangle 2 is:{rect2.area()}")
print("\nNow comparing the rectangles")
if rect1<rect2:
    print("The area of rectangle1 is less than rectangle2")
elif rect2<rect1:
    print("The area of rectangle2 is less than rectangle1")
else:
    print("Both the rectangles are of same area")
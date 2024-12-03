class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def display(self):
        print(f"Area of rectangle:{self.area()}")
        print(f"Perimeter of rectangle:{self.perimeter()}")
    def compare_area(self,other):
        if self.area()==other.area():
           print("\nRectangles are equal in area.")
        elif self.area()>other.area():
           print(f"\nRectangle 1 is greater in area than rectangle 2.")
        else:
           print("\nRectangle 2 is greater in  area than rectangle 1.")
print("Enter dimensions of the first rectangles")
length1=int(input("Enter length 1:"))
breadth1=int(input("Enter breadth 1:"))
rect1=Rectangle(length1,breadth1)
rect1.display()
print("\nEnter the dimension of the 2nd rectangle:")
length2=int(input("Enter length 2:"))
breadth2=int(input("enter breadth2:"))
rect2=Rectangle(length2,breadth2)
rect2.display()
rect1.compare_area(rect2)
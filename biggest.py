a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
if a >= b and a >= c:
    n = a
elif b >= a and b >= c:
        n = b
else:
  n = c
print(f"The biggest number is:{n}")
nn = n ** 2
nnn = n ** 3
result = n + nn + nnn
print(f"n + nn + nnn = {n} + {nn} + {nnn} = {result}")
pi = 3.14
r = n
area = pi * r ** 2
perimeter = 2 * pi * r
volume = 3 * pi * r ** 3
print(f"The area of circle is {area}")
print(f"The perimeter of circle is {perimeter}")
print(f"The volume of sphere is {volume}")
#Python Program for Program to find area of a circle
def area(r) :
 PI = 3.142
 return PI*(r*r)

radius = float(input("Enter the radius of a circle : "))
print("The area of a circle is : ",area(radius))

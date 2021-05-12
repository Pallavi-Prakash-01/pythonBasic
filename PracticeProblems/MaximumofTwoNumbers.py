#Maximum of two numbers in Python
num1 = float(input("Enter the value for num1 : "))
num2 = float(input("Enter the value for num2 : "))
if num1 == num2 :
  print("The entered values are equal")
elif num1 > num2 :
  print("The maximum of two numbers is : ", num1)
else : print("The maximum of two numbers is : ", num2)
  
 #Another Simple Solution
print("The maximum of two numbers is using max() : ",max(num1,num2))

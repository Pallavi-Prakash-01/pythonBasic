#Python Program to check Armstrong Number
def order(n):
  x=0
  while(n%10 != 0):
    x=x+1
    n=int(n/10)
  return x

def armstrong(n):
  x=order(n)
  sum=0
  while(n!=0):
    sum = sum + (n%10)**x
    n = int(n/10)
  return sum

n = int(input("Enter a number for armstrong validation : "))
res = armstrong(n)
if res == n :
  print("The Entered number is an Armstrong number")
else : print("The Entered number is not an Armstrong number") 

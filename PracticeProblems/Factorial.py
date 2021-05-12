#Python Program for factorial of a number
def fact(n) :
  if n==0 or n==1 : return 1 
  else :
    return n * fact(n-1) 

n=int(input("enter value for n : "))   
prod = fact(n)
print("The factorial of ", n ,"is : ",prod)

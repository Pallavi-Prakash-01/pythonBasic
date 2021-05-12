#Python Program for compound interest (Amount = P(1 + R/100)^t CI = amount-principle amount)
def ci(p,t,r):
  amount=p*(pow((1+r/100),t)) #amount = p*((1+r/100)**t) both statements are same
  return amount-p

p=float(input("Enter principle amount : "))
t=float(input("Enter time : "))
r=float(input("Enter Raote of interest : "))
print("Compound Interest is : ", ci(p,t,r))

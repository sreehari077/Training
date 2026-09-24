n=int(input("Enter the No:"))
large=0
while n>0:
  rem=n%10
  if rem>large:
    large=rem
  n=n//10
print("Lareg number=",large)

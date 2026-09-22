n=int(input("Enter the number of monkeys:"))
k=int(input(" Number of eatable Bananas:"))
j=int(input(" Number of eatable Peanuts:"))
m=int(input("Total number of Bananas:"))
p=int(input("Total number of Peanuts:"))
if k==0 or j==0:
  print("Invalid")
else:
  n=n-(m//k+p//j)
  if m%k!=0 or p%j!=0:
    n=n-1
  print("No.of monkeys in tree",n)

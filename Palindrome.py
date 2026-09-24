n=int(input("Enter the Number:"))
temp=n
rev=0
while n>0:
  rem=n%10
  rev=rev*10+rem
  n=n//10
if temp==rev:
  print("Number is Palindrome")
else:
  print("Number is not Palindrome")

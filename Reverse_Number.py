a=int(input("Enter your number:"))
rev=0
while a>0:
  num=a%10
  rev=rev*10+num
  a=a//10
print("Reversed number is:",rev)

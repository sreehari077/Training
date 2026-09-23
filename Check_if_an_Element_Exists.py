n=int(input("Enter the no.of Elements:"))
num=[]
key=1
for i in range(n):
  x=int(input("Enter the elements:"))
  num.append(x)
find=int(input("Enter Elements you needed to find"))
for i in range(n):
  if find==num[i]:
    print("Elements is present")
    key=0
    break
if key==1:
  print("Element is not found")

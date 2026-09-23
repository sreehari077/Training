n=int(input("enter the no of elements:"))
arr=[]
for i in range(n):
  arr.append(int(input("enter the elements:")))
print("reversed:",arr[::-1])

N1=int(input("enter the no of strong positions on road A:"))
N2=int(input("enter the no of strong positions on road B:"))
a=[int(input("enter the strong positions on road A:")) for i in range(N1)]
b=[int(input("enter the strong positions on road B:")) for i in range(N2)]
s=sorted(set(a+b))
print(s)
N=len(s)
if N%2==1:
  print(s[N//2])
else:
  print((s[N//2-1]+s[N//2])/2)

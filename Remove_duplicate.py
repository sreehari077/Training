s = input("Enter a string: ")
st = ""
for i in s:
    if i not in st:
        st += i
print(st)

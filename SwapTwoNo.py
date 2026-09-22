a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print("\nUsing temp")
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)
print("\nUsing comma")
a, b = b, a
print("a =", a)
print("b =", b)
print("\nUsing + and -")
a = a + b
b = a - b
a = a - b
print("a =", a)
print("b =", b)
print("\nUsing ^")
a = a ^ b
b = a ^ b
a = a ^ b
print("a =", a)
print("b =", b)

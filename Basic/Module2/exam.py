x = int(input("x: "))
y = int(input("y: "))

x = x % y
print(x)
x = x % y
print(x)
y = y % x
print(y)

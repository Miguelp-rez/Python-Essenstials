print("ñ".isascii())

a = "ñ".encode("UTF-8")
print(a) #0xC3B1

print(dir(str))

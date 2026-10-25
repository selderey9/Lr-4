a = input("Enter (a) letter(lowercase) or number:")
b = input("Enter (b) letter(lowercase) or number:")

start = ord(a)
end = ord(b)

for i in range(start, end + 1):
    print(chr(i))


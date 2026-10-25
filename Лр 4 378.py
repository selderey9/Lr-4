a = input("Enter your word:")
le = (len(a) + 1) // 2
result = a[le:] + a[:le]
print(result)

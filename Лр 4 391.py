s = input("Enter your phrase:")
numbers = []
word = ""
for part in s.split():
    for ch in part:
        if ch.isdigit():
            word += ch
        elif word:
            numbers.append(word)
            word = ""
    if word:
        numbers.append(word)
        word = ""
print(", ".join(numbers))

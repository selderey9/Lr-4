while True:
    try:
        s = input()
    except EOFError:
        break
    words = s.split()
    longest = ""

    for word in words:
        word = word.strip(".,!?;:()[]")
        if len(word) > len(longest):
            longest = word
    print(longest)

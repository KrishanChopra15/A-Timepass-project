range = range(32,128)
empty = []
inp = input("Enter a word:")
l = list(inp)
def loop():
    for i in range:
        if len(empty) == len(inp):
            break
        else:
            work = "".join(empty)
            print(f"{work}{chr(i)}")
            if chr(i) == l[len(empty)]:
                empty.append(chr(i))
                loop()
loop()
final = "".join(empty)
print(f"\n\n{final}\n")

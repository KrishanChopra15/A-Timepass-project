rang = range(32,128)
empty = []
inp = input("Enter a word:")
lis = list(inp)
def loop():
    for i in rang:
        if len(empty) == len(inp):
            break
        else:
            print(*empty,chr(i))
            if chr(i) == lis[len(empty)]:
                empty.append(chr(i))
                loop()
loop()
print("\n\n",*empty,"\n")

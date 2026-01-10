decimal = input("Enter a number:")
binary = []

def loop(X):
    quotent = int(X/2)
    remainder = X % 2
    binary.append(remainder)
    if quotent == 0:
        binary.append(0)
    elif quotent == 1:
        binary.append(1)
    elif quotent == 2:
        binary.extend((0,1))
    elif quotent > 2:
        X = quotent 
        loop(X)


if decimal.isdigit() is True:
    if decimal == 0:
        binary.append(0)
    elif decimal == 1:
        binary.append(1)
    elif int(decimal) > 1:
        loop(int(decimal))
else:
    print("\nPlease enter a valid number.")

finalbinary = (''.join(str(x) for x in binary[::-1]))
print(f"\n{finalbinary}")
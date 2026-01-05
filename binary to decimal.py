binary = input ("Enter a binary number:")
binarylen = len (binary)
decimal = 0
if binary.isdigit() is True:
    for i in range (binarylen,0,-1):
        number = int (binary[-i])
        if number == 1:
            decimal += (2**(i-1))
        elif number not in (1,0):
            print ("Enter a valid binary number")
            decimal = ""
            break
else:
    print ("Enter a valid binary number")
    decimal = ""
print (decimal)
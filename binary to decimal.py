binary = input ("Enter a binary number:")
binarylen = len (binary)
decimal = 0
for i in range (binarylen,0,-1):
    number = int (binary[-i])
    if number == 1:
        decimal += (2**(i-1))
print (decimal)
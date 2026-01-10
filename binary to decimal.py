binary = input ("Enter a binary number:")              
binarylen = len (binary)                               
decimal = 0
if binary.isdigit() is True:
    for i in range (binarylen,0,-1):                   
        if int(binary[-i]) == 1:                       
            decimal += (2**(i-1))                      
        elif int(binary[-i]) not in (1,0):
            print ("\nEnter a valid binary number")
            decimal = ""
            break
else:
    print ("\nEnter a valid binary number")
    decimal = ""
print (f"\n{decimal}")

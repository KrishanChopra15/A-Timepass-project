import math
number = int(input("Enter a number:"))
l = []
for num in range(number):
    l.append(num + 1)

print("Factorial of {0} is: {1}".format(number,math.prod(l)))

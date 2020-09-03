import math

def is_valid_triangle(a, b, c):
    if a > b + c:
        return False
    if b > a + c:
        return False
    if c > a + b:
        return False

    return True

#Get input, a, b, c
a= float(input(("Enter a:")))
b= float(input(("Enter b:")))
c= float(input(("Enter c:")))

if not is_valid_triangle(a, b, c):
    print("Invalid values for triangle sides")
else:
    s=(a+b+c)/2
    area = math.sqrt(s*(s - a)*(s - b)*(s - c))
    print('The triangle area is :' + str(area))
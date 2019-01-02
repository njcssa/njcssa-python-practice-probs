#######################################################################################
#4.1

print("Enter number 1:")
n1 = input()
print("Enter number 2:")
n2 = input()
print("Enter number 3:")
n3 = input()

if(n1 >= n2 and n1>=n3):
    print(n1, "is the largest")
elif(n2 >= n1 and n2>=n3):
    print(n1, "is the largest")
elif(n3 >= n2 and n3>=n1):
    print(n1, "is the largest")

#######################################################################################
#4.5

#gathering user input
print("Enter a side 1:")
s1 = int(input())
print("Enter a side 2:")
s2 = int(input())
print("Enter a side 3:")
s3 = int(input())

#decision-making
if s1+s2<s3 or s1+s3<s2 or s2+s3<s1 or s1<=0 or s2<=0 or s3<=0:
    print("This isn't a real triangle!")
elif s1==s2 and s2==s3 :
    print("This is an equilateral triangle!")
elif (s1==s2 and s2!=s3) or (s1!=s2 and s2==s3):
    print("This is a isoceles triangle!")
else:
    print("This is a scalene triangle")

#######################################################################################
#4.6

import math

print("Enter a:")
a = float(input())
print("Enter b:")
b = float(input())
print("Enter c:")
c = float(input())

result = math.pow(b, 2) - 4 * a * c

if result > 0:
    r1 = (-b + math.sqrt(result)) / (2 * a)
    r2 = (-b - math.sqrt(result)) / (2 * a)
    print("The roots are ", r1 , " and " , r2)
elif result == 0:
    r1 = -b / (2 * a)
    print ("The root is ", r1)
else:
    print("The equation has no real roots.")


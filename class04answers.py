#######################################################################################
#4.0

thing = "Hello"
n2 = input()
if n2==thing:
    print("True")
else: 
    print("False")
thing2 = 21
n = int(input())
if(n==thing2):
    print("True")
else:
    print("False")

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
#4.2

grade = round(float(input("Enter a grade:"))+0.1)
if(grade>=90):
     print('A', end='')
     grade -= 90
elif(grade>=80):
    print('B', end='')
    grade -= 80
elif(grade>=70):
    print('C', end='')
    grade -= 70
elif(grade>=60):
    print('D', end='')
    grade -= 60
else:
    print('F')
    grade = -1

if(grade!=-1):
    if(grade>=7):
        print('+')
    elif(grade>=3):
        print('')
    else:
        print('-')
   
#######################################################################################
#4.3

s1 = input("Enter card:")
s2 = input("Enter card:")
s3 = input("Enter card:")
s4 = input("Enter card:")
s5 = input("Enter card:")

if(s1=='J'):
    n1 = 11
else:
    n1 = int(s1)
if(s2=='J'):
    n2 = 11
else:
    n2 = int(s2)
if(s3=='J'):
    n3 = 11
else:
    n3 = int(s3)
if(s4=='J'):
    n4 = 11
else:
    n4 = int(s4)
if(s5=='J'):
    n5 = 11
else:
    n5 = int(s5)

if(n1+1 == n2 and n2+1 == n3 and n3+1 == n4 and n4+1 == n5):
    print("Straight")
else:
    print("Not a straight")

#######################################################################################
#4.4

op = int(input("Enter operation (0-3):"))
n1 = int(input("First Number:"))
n2 = int(input("Second Number:"))

if(op==0):
    print(n1+n2)
if(op==1):
    print(n1-n2)
if(op==2):
    print(n1*n2)
if(op==3):
    print(n1/n2)

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


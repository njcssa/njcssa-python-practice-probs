#######################################################################################
# 8.1

counter = 0
while counter < 10:
    print(counter)
    counter += 1

for i in range(0, 10):
    print(i)

#######################################################################################
# 8.2
print("Enter number1: ")
n1 = int(input())
print("Enter number2: ")
n2 = int(input())
total = 0

for i in range(0, n2):
    total += n1
print(total)

#######################################################################################
# 8.3

print("Enter the number: ")
number = int(input())
print("Enter the power: ")
power = int(input())
answer = 1

for i in range(0, power):
    answer *= number
print("=" + str(answer))

#######################################################################################
# 8.4

for i in range(0, 3):
    for j in range(0, 2):
        print(j)


#######################################################################################
# 8.5

print("Enter rows: ")
length = int(input())
print("Enter cols: ")
width = int(input())

line = ""

for i in range(0, length):
    for j in range(0, width):
        line += "*"
    print(line)
    line = ""


#######################################################################################
# 8.6

largest = -1
for i in range(0, 3):
    user_number = int(input())
    if i == 0:
        largest = user_number
    else:
        if largest < user_number:
            largest = user_number
    
print("The largest number is {}".format(largest))


#######################################################################################
# 8.7a

print("enter num1: ")
num1 = int(input())
print("enter num2: ")
num2 = int(input())

line = ""

for i in range(1, num1):
    for j in range(1, num2):
        line += "{}x{}={}\t".format(i, j, i*j)
    print(line)
    line = ""

#######################################################################################
# 8.7b
import math

print("enter num1: ")
num1 = int(input())
print("enter num2: ")
num2 = int(input())

line = ""

for i in range(1, num1):
    for j in range(1, num2):
        line += "{}^{}={} \t ".format(i, j, math.pow(i, j))
    print(line)
    line = ""

#######################################################################################
# 8.8
# they could also accomplish this using string addition

print("Enter amount of 1s: ")
number = int(input())
start = 1
tens = 1
for i in range(0, number):
    print(start)
    tens *= 10
    start += tens


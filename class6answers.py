#######################################################################################
# 6.1

counter = 0
while counter <= 100:
    print(counter)
    counter += 1

#######################################################################################
# 6.2

total = 0
counter = 0
while counter < 10:
    total += float(input())
    counter += 1

print("Average is {}".format(total / 10))

#######################################################################################
# 6.3

total = 1
number = 4
while number > 1:
    total *= number
    number -= 1

print(total)

#######################################################################################
# 6.4

print("please enter num1: ")
num1 = int(input())
print("please enter num2: ")
num2 = int(input())

largest_factor = 1

# checks which number greater so don't do extra checks
# not necessary to solve problem

i = 1
if num1 <= num2:
    while i <= num1:
        if num2 % i == 0 and num1 % i == 0 and i > largest_factor:
            largest_factor = i
        i += 1
else:
    while i <= num2:
        if num1 % i == 0 and num2 % i == 0 and i > largest_factor:
            largest_factor = i
        i += 1

print("The GCF of {} and {} is {}".format(num1, num2, largest_factor))

#######################################################################################
# 6.5

total = 0
number = input()
counter = 0
while number != "stop":
    total += int(number)
    number = input()
    counter += 1

if counter == 0:
    print("no average")
else:
    print("The average of the numbers is {}".format(total/counter))

#######################################################################################
# 6.6

print("how many steps?")
steps = int(input())

string = ""
counter = 0
while counter < steps:
    string += "*"
    print(string)
    counter += 1


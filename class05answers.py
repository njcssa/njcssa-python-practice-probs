#######################################################################################
# 5.1

while True:
    print("infinite")

#######################################################################################
# 5.2

counter = 1
while counter <= 10:
    print(counter)
    counter += 1

#######################################################################################
# 5.3

counter = 0
while counter <= 100:
    print(counter)
    counter += 2


#######################################################################################
# 5.4

counter = 100
while counter > 0:
    print(counter)
    counter -= 3


#######################################################################################
# 5.5

total = 0
inp = int(input())
while not inp == -1:
	print("{} + {} = {}".format(total, inp, total+inp))
	total = total + inp
	inp = int(input())

#######################################################################################
# 5.6

counter = 0
while counter < 1000:
    if counter == 100:
        print("exited")
        break
    print(counter)
    counter += 1


#######################################################################################
# 5.7

a = 0
b = 0
c = 0

while a < 100 and b < 100 and c < 100:
    print("a: {} b: {} c: {}".format(a, b, c))
    a += 1
    b += 2
    c += 3

#######################################################################################
# 5.8

counter1 = 1
counter2 = 1
while counter1 <= 10:
    while counter2 <= 3:
        print("counter1: {} counter2: {}".format(counter1, counter2))
        counter2 += 1
    counter2 = 1
    counter1 += 1
#######################################################################################
# 5.9

string = "this is a cool string"
length = len(string)
i = 0
while i < length:
    print(string[i:i+1])
    i += 1


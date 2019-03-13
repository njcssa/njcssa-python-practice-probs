

#######################################################################################
# 1.1
# Use a while loop to print out the numbers 1-10

counter = 1
while counter <= 10:
    print(counter)
    counter += 1

#######################################################################################
# 1.2
# Use a for loop to print out the numbers 1-10

for i in range(1, 11):
    print(i)

#######################################################################################
# 1.3
# Use a for loop to loop through the list below and print out all the numbers. Print
# out the numbers using list indexes (list[index]) instead of by value.

some_list = [2, 4, 6, 8, 10]
for i in range(len(some_list)):
    print(some_list[i])


#######################################################################################
# 1.4
# Use a for loop to add 3 to all the numbers in this list. This means that the list
# should be changed. Then print out all the numbers in the list.

num_list = [3, 4, 5, 9, 10, 11]
for i in range(len(num_list)):
    num_list[i] = num_list[i] + 3
    print(num_list[i])


#######################################################################################
# 1.5
# Use a while loop to add 10 items to an empty list.

empty = []
counter = 0
while counter < 10:
    empty.append(1)
    counter += 1


#######################################################################################
# 1.6
# Use a for loop to loop through this list and find what index the value stored in the
# variable dog exists at. Print the index.

dog = "dog"
some_list = ["cat", "poodle", "mouse", "dog", "human", "elephant", "moose"]
for i in range(len(some_list)):
    if some_list[i] == dog:
        print(i)


#######################################################################################
# 1.7
# Make a for loop which prints the numbers negative 10 to negative 50 inclusive.

for i in range(-10, -51, -1):
    print(i)

#######################################################################################
# 1.8
# Using a for loop, delete the elements in the list below that are at even list indexes.
# Print out the new list after you are done deleting.

some_list = [4, True, "dog", "man", 2.3, False, "nice", "great", 2, 6, 10]

for i in range(len(some_list)):
    if i % 2 == 0:
        del some_list[i]

print(some_list)







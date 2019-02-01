#######################################################################################
#12.1

consanants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
string = "school"

if string[0:1].lower() in consanants:
    print("String starts with consanant") 
else:
    print("String starts with vowel")

#######################################################################################
#12.2

vowels = ["a", "e", "i", "o", "u"]
string = "cat"

if string[0:1].lower() in vowels:
    print("String starts with a vowel")
else:
    print("String starts with a consanant")

#######################################################################################
#12.3

input_string = input("Please enter a word you want to convert to pig latin: ")
vowels = ["a", "e", "i", "o", "u"]
pig_latin = ""

if input_string[0:1].lower() in vowels:
    pig_latin = input_string + "way"
else:
    pig_latin = input_string[1:] + input_string[0:1] + "ay"

print("Changed word: {}".format(pig_latin))


#######################################################################################
#12.4

input_string = input("Please enter a string you want to convert to pig latin: ")
if input_string.find(".") != -1: # removes period
    input_string = input_string[0:input_string.find(".")]

string_list = input_string.split(" ")
vowels = ["a", "e", "i", "o", "u"]
result = ""
for i, word in enumerate(string_list):
    if word[0:1].lower() in vowels:
        result += word + "way "
    else:
        result += word[1:] + word[0:1] + "ay "
    if i + 1 == len(string_list): # extra
        result = result[0:-1] + "."

print(result)



#######################################################################################
#12.5
words = []
input_words = input("input some words separated by spaces: ")

current = 0
i = 0
while current <= len(input_words):
    while i <= len(input_words) and input_words[i:i+1] != " ":
        i += 1
    words.append(input_words[current:i])
    current = i + 1
    i = i + 1
print(words)

#######################################################################################
#12.6
li = [5,6,2,3,4,5,2]
lowest = 2e9
highest = -2e9
for i in li:
    if lowest>i:
        lowest = i
    if highest<i:
        highest = i

print("Lowest: " + str(lowest) + '\nHighest: ' + str(highest))



#######################################################################################
#12.7

orig = [2,3,5,7,4,5,767,8,6,7,567,55]
st = list()

while len(orig)>0:
    hold = min(orig)
    st.append(hold)
    orig.remove(hold)

print(st)

#######################################################################################
#12.8

orig = [[2,3],[4,5],[6,7]]
print(orig)
mid = list()

for i in range (0, len(orig)):
    for j in range (0, len(orig[0])):
        mid.append(orig[i][j])
    
inv = list()
for i in range (0, len(orig[0])):
    hold = list()
    for j in range (0, len(orig)):
        hold.append(mid[i*len(orig) + j])
    inv.append(hold)

print(inv)

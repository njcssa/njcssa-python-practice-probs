#######################################################################################
# 11.1
list1 = [0,1,2,3,4,5,6,7,8,9]
print(list1.index(1))

#######################################################################################
# 11.2
list1 = []
list1.append(0)
print(list1)

#######################################################################################
# 11.3
list1 = []
for i in range(10):
    list1.append(i)
print(list1)

#######################################################################################
# 11.4
list1 = [0,1,2,3,4,5,6,7,8,9]
list1.remove(0)
print(list1)


#######################################################################################
# 11.5
list1 = ['DEF', 'JkL', 'GhI', 'ABC']
list1.sort()
print(list1)

#######################################################################################
# 11.6
list1 = [22,32,1,2,3,54,323,4,4,234]
list1.sort()
print(list1)

#######################################################################################
# 11.7
list1 = [22,32,1,2,3,54,323,4,4,234]
list1.sort(reverse=True)
print(list1)

#######################################################################################
# 11.8
s = 'NJCSSA'
print(s[0:2])

#######################################################################################
# 11.9
s = "njcssa.org"
print(list(s))

#######################################################################################
# 11.10
s = 'abcdef'
list1 = []
for i in range(len(s)):
    list1.append(s[i:i+1])
list1.append('g')
list1.append('h')
print(list1)

#######################################################################################
# 11.11
s = 'abcdef'
t = slice(3)
print(s[t])

#######################################################################################
# 11.12
#Sample Answer
s = 'NJCSSA'
print(s)
l = list(s)
print(l)
l.append('.org')
print(l)
print(s[0:2])
print(s[slice(2,6)])


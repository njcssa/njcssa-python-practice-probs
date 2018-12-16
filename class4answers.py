######################################################################
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

#######################################################################################
#12.2

orig = [2,3,5,7,4,5,767,8,6,7,567,55]
st = list()

while len(orig)>0:
    hold = min(orig)
    st.append(hold)
    orig.remove(hold)

print(st)

#######################################################################################
#12.2
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
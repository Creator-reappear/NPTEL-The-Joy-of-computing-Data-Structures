L=input().split()
L=[int(float(x)) for x in L]
cmp=0

for x in L:
    a=L.count(x)
    if (a>1):
        cmp+=1

if(cmp!=0):
    print("True")
else:
    print("False")

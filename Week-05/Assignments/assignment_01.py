L=input().split()
a=[int(float(x)) for x in L]

b=[]
for x in range(len(a)):
    count=0
    for y in range(len(a)):
        if(a[y]==a[x]):
            count=count+1
    b.append(count)

c=max(b)
d=[]
for x in range(len(a)):
    if(b[x]==c):
        d.append(a[x])

c=min(d)
print(c)

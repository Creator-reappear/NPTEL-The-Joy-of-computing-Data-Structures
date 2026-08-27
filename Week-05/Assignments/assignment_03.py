def exactly_two(L):
    a=[int(float(x)) for x in L]

    b=[]
    for x in range(len(a)):
        count=0
        for y in range(len(a)):
            if(a[y]==a[x]):
                count=count+1
        if count==2:
            b.append(a[x])

    d=[]
    for x in b:
        if x not in d:
            d.append(x)

    d.sort()
    if(len(b)==0):
        print("-1")
    else:
        print(*d)

L=input().split()
exactly_two(L)

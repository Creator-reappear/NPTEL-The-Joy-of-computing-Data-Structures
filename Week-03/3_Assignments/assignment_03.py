from statistics import mean
a=input().split()
b=[float(x) for x in a]
avg=mean(b)
count=0
for i in range(len(a)):
    if b[i]>avg:
        count+=1  

print(count)

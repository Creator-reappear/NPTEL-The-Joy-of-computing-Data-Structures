# 
N = int(input().strip())
a=[]

a= input().strip().split()
found=-1
b = input().strip()

for i in range(N):
    if a[i]==b:
        print(i)
        found=0
        break

if found<0:
    print("-1")

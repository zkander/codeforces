n=5
rc=3
cc=3
r=0
c=0
m=0
for i in range(1,n+1):
    a,b,c,d,e=map(int,input().split())
    if a==1:
        r=i
        c=1
        break
    if b==1:
        r=i
        c=2
        break
    if c==1:
        r=i
        c=3
        break
    if d==1:
        r=i
        c=4
        break
    if e==1:
        r=i
        c=5
        break
while c!=cc:
    if c>cc:
        c-=1
    if c<cc:
        c+=1
    m+=1
while r!=rc:
    if r>rc:
        r-=1
    if r<rc:
        r+=1
    m+=1
    
print (m)
n = int(input())
ans = []
for i in range (0,n):
    count=0
    k = int (input())
    count=k
    for j in range (0,k):
        l,b = map(int,input().split())
        if (l-b<=0):
            count-=1
    ans.append(count)

for i in range (0,len(ans)):
    print (ans[i])
    
        
    
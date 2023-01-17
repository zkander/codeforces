n = int(input())
sum=0
for i in range(0,n):
    p,v,t=map(int,input().split())
    if p==1 and v==1 or p==1 and t==1 or v==1 and t==1:
        sum+=1
        
print (sum)        
        
    
        
    
    
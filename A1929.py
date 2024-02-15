t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    sum = 0 
    for i in range (len(a)-1, 0, -1):
       sum += a[i] - a[i-1]
    print(sum)
        
        
    
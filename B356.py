n, b = map(int, input().split())
arr = list(map(int, input().split()))

n -= 1
b -= 1
count = 0
for i in range(n+1):
    
    if arr[i] == 1:
        theOtherCity = b + (b - i)
        if (-1 < theOtherCity <= n):
            if arr[theOtherCity] == 1:
                count += 1
                i = theOtherCity
                continue
        else:
            count += 1
    

print(count)

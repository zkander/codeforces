
n = int(input())
for _ in range(n):
    k = int(input())
    arr = list(map(int, input().split()))
    seq = 0
    for i in range(len(arr)):
        if (arr[i] == (seq+1)):
            seq = arr[i] + 1
        else:
            seq+=1
    print(seq)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
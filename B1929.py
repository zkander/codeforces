t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    if ((4*n-2) == k):
        print(int(2*n))
    elif (k%2 == 0):
        print(int(k/2))
    else:
        print(int(k/2+1))

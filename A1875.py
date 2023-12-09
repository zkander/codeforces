

n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    arr.sort()
    for i in range(c):
        if (b + arr[i]) <= a:
            b += arr[i]
        else:
            count += (b-1)
            b = min(1 + arr[i], a)
    count += b
    print(count)

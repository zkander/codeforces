x = int(input())

for _ in range(x):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = 0
    y = 0

    for i in range(1, n):
        if a[i] < a[x]:
            x = i

    for i in range(1, m):
        if b[i] > b[y]:
            y = i

    if a[x] < b[y]:
        a[x], b[y] = b[y], a[x]

    if k % 2 == 0:

        x = 0
        y = 0

        for i in range(1, n):
            if a[i] > a[x]:
                x = i

        for i in range(1, m):
            if b[i] < b[y]:
                y = i

        a[x], b[y] = b[y], a[x]

    ans = sum(a)
    print(ans)

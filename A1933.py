t = int(input())

for _ in range(t):

    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if (a[i] < 0):
            a[i] = -a[i]

    print(sum(a))

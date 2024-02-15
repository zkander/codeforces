import math


def solve():
    k, x, a = map(int, input().split())

    if a <= x:
        print("NO")
        return

    arr = [0] * (x + 1)
    arr[0] = 1
    lim = 1
    a -= 1

    for i in range(1, x + 1):
        req = math.ceil(1.0 * (lim + 1) / (k - 1))
        arr[i] = req
        a -= req
        if a < 0:
            print("NO")
            return
        lim += req

    print("YES")


t = int(input())
for _ in range(t):
    solve()

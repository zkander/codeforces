t = int(input())


def sumDigits(n):
    strr = str(n)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)


for _ in range(t):
    x, k = map(int, input().split())
    f = False
    while True:
        sums = sumDigits(x)
        if sums % k == 0:
            break
        x += 1

    print(x)

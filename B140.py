n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dict = {}

for i in range(n):
    dict[a[i]] = i

v = 0
p = 0

for k in range(m):
    v += dict[b[k]] + 1
    p += n - dict[b[k]]

print(v, p)

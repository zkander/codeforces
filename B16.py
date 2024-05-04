n, m = map(int, input().split())

pair = {}

for _ in range(m):
    a, b = map(int, input().split())
    if b in pair.keys():
        temp = pair[b] + a
        pair[b] = temp
    else:
        pair[b] = a

pair = dict(sorted(pair.items(), key=lambda item: item[0], reverse=True))

matches = 0

for key, value in pair.items():
    if m < 1:
        break
    if value <= n:
        matches += key * value
        n -= value
    else:
        matches += n * key
        n = 0
        break


print(matches)

n = int(input())
arr = list(map(int, input().split()))


max = 0
max_index = 0
for i in range(n):
    count = 0
    index_b = i
    index_a = i
    before = i - 1
    after = i + 1

    while (before > -1):
        if arr[index_b] >= arr[before]:
            count += 1
            index_b = before
            before -= 1
        else:
            break
        
    while (after < n):
        if arr[index_a] >= arr[after]:
            count += 1
            index_a = after
            after += 1
        else:
            break

    if max <= count:
        max = count
        
print(max + 1)

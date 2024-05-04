from collections import defaultdict

arr = []

for _ in range(3):
    w = str(input())
    arr.append(w)


dictMoreThan = defaultdict(int)
dictLessThan = defaultdict(int)

for i in range(len(arr)):
    if arr[i][1] == ">":
        dictMoreThan[arr[i][0]] += 1
        dictLessThan[arr[i][2]] += 1
for i in range(len(arr)):
    if arr[i][1] == "<":
        dictLessThan[arr[i][0]] += 1
        dictMoreThan[arr[i][2]] += 1

results = {}

for i in set(dictMoreThan.keys()) | set(dictLessThan.keys()):
    diff = dictMoreThan[i] - dictLessThan[i]
    results[i] = diff

results = dict(sorted(results.items(), key=lambda item: item[1]))


# check for cycles
if results["A"] == results["B"] == results["C"] == 0:
    print("Impossible")
    exit()

for i in results.keys():
    print(i, end="")

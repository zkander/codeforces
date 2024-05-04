n = int(input())

def sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

count = 0 
while(len(str(n)) > 1):
    n = sum(n)
    count += 1

print(count)
    



 
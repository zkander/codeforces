n = int(input())
ans = []

for i in range (0,n):
    first = list(str(input()))
    second = list(str(input()))
    third = list(str(input()))
    
    if (first[0]==first[1]==first[2] and first[0]!="."):
        ans.append(first[0])
    elif (second[0]==second[1]==second[2] and second[0]!="."):
        ans.append(second[0])
    elif (third[0]==third[1]==third[2] and third[0]!="."):
        ans.append(third[0])
    
    elif (first[0]==second[0]==third[0] and first[0]!="."):
        ans.append(first[0])
    elif (first[1]==second[1]==third[1] and first[1]!="."):
        ans.append(first[1])
    elif (first[2]==second[2]==third[2] and first[2]!="."):
        ans.append(first[2])
    
    elif (first[0]==second[1]==third[2] and first[0]!="."):
        ans.append(first[0])
    elif (first[2]==second[1]==third[0] and first[2]!="."):
        ans.append(first[2])
    else:
        ans.append("DRAW")
    


for i in range (0,len(ans)):
    print (ans[i])
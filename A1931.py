
dic = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}

t = int(input())
for _ in range(t):
    n = int(input())
    x = n // 26

    if (x == 0 or n == 26):
        print('a' + 'a' + dic[n-2])
    else:
        if (x == 2):
            print(dic[n % 26] + 'z' + 'z')
        elif (x == 1):
            print('a' + dic[(n % 26)-1] + 'z')
        elif (x == 3):
            print('z' + 'z' + 'z')

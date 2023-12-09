from collections import defaultdict


t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    unique_combinations1 = set()

  
    for op_x in [-a, a]:
        for op_y in [-b, b]:
            new_x_1 = x1 + op_x
            new_y_1 = y1 + op_y
            unique_combinations1.add((new_x_1, new_y_1))

            new_x_2 = x1 + op_y
            new_y_2 = y1 + op_x
            unique_combinations1.add((new_x_2, new_y_2))

            new_x_3 = x1 + op_x
            new_y_3 = y1 - op_y
            unique_combinations1.add((new_x_3, new_y_3))

            new_x_4 = x1 - op_y
            new_y_4 = y1 + op_x
            unique_combinations1.add((new_x_4, new_y_4))

            new_x_5 = x1 - op_x
            new_y_5 = y1 + op_y
            unique_combinations1.add((new_x_5, new_y_5))

            new_x_6 = x1 + op_y
            new_y_6 = y1 - op_x
            unique_combinations1.add((new_x_6, new_y_6))

            new_x_7 = x1 - op_x
            new_y_7 = y1 - op_y
            unique_combinations1.add((new_x_7, new_y_7))

            new_x_8 = x1 - op_y
            new_y_8 = y1 - op_x
            unique_combinations1.add((new_x_8, new_y_8))

    unique_combinations2 = set()

    for op_x in [-a, a]:
        for op_y in [-b, b]:
            new_x_1 = x2 + op_x
            new_y_1 = y2 + op_y
            unique_combinations2.add((new_x_1, new_y_1))

            new_x_2 = x2 + op_y
            new_y_2 = y2 + op_x
            unique_combinations2.add((new_x_2, new_y_2))

            new_x_3 = x2 + op_x
            new_y_3 = y2 - op_y
            unique_combinations2.add((new_x_3, new_y_3))

            new_x_4 = x2 - op_y
            new_y_4 = y2 + op_x
            unique_combinations2.add((new_x_4, new_y_4))

            new_x_5 = x2 - op_x
            new_y_5 = y2 + op_y
            unique_combinations2.add((new_x_5, new_y_5))

            new_x_6 = x2 + op_y
            new_y_6 = y2 - op_x
            unique_combinations2.add((new_x_6, new_y_6))

            new_x_7 = x2 - op_x
            new_y_7 = y2 - op_y
            unique_combinations2.add((new_x_7, new_y_7))

            new_x_8 = x2 - op_y
            new_y_8 = y2 - op_x
            unique_combinations2.add((new_x_8, new_y_8))

  

    count = 0

    for combination in unique_combinations1:
        if combination in unique_combinations2:
            count += 1

    print(count)

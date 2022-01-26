a =  [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

# 3번째 인자로 정렬하기
a.sort(key=lambda x:x[2])
# print(a)

# print(a[0][0:2])

from itertools import combinations
from re import sub

# print(list(combinations(a, 3)))
subset = list(combinations(a, 3))

print(subset)


for x in range(len(subset)):
    temp = []
    ans = []
    for y in range(3):
        # print(subset[x][y][0:2])
        temp.extend(subset[x][y][0:2])
        ans.extend(subset[x][y][2:])
    print(set(temp))

    target = set(temp)

    if len(target) == 4:
        print(sum(ans))
        break


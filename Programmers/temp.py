from collections import deque
from re import template

temp = deque()
time = deque()

temp.appendleft(3)
temp.appendleft(2)
temp.appendleft(1)

# for i in range(len(temp)):
#     temp[i] += 1

# print(temp)

print(sum(time))
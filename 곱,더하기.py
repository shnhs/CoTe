# 그리디 - 곱하기 혹은 더하기

# n = map(int, list(input())) 

n = list(input())
result = int(n[0])

for i in range(1, len(n)):
    # print(n[i])
    if int(n[i]) <= 1 or result == 0:
        result += int(n[i])
    else:
        result *= int(n[i])

print(result)
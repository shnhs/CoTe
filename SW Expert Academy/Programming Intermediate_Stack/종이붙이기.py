n = open("SW Expert Academy\Programming Intermediate_Stack\input.txt", "r")

T = int(n.readline())

for test_case in range(1, T + 1):
    # 문자열 받기
    M = int(n.readline())

    memo = [0,1,3]
    index = int(M/10)

    for i in range(3, index+1):
        if index%2 == 1: # 홀수일때
            memo.append(4*memo[i-2] + 1) 
        else: # 짝수일때
            memo.append(4*memo[i-2] - 1)

    ans = memo[index]

    print(f'#{test_case} {ans}')
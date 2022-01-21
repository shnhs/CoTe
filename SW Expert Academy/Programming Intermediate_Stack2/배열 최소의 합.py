import sys

n = open("SW Expert Academy\Programming Intermediate_Stack2\input.txt", "r")

T = int(n.readline())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N = int(n.readline())  # NxN 배열 입력
    box = []

    for i in range(N):
        temp = list(map(int, n.readline().split()))
        box.append(temp)

    # print(f'#{test_case} {ans}')
from math import ceil
from tkinter import font


n = open("SW Expert Academy\Programming Intermediate_String\input.txt", "r")

T = int(n.readline())

for test_case in range(1, T + 1):

    # N : N x N 의 글자판
    # M : M길이의 회문 찾기
    N, M = map(int, n.readline().split())
    
    # 문자열을 글자 하나씩 리스트로 넣음
    box = []
    for _ in range(N):
        box.append(list(n.readline().rstrip()))
    
    # 가로 탐색
    for i in range(N):
        for j in range(N):
            if M % 2 == 1:
                front_part = ''.join(reversed(box[i][j:j+int(M/2)]))
                back_part = ''.join(box[i][j+1+int(M/2):j+1+2*int(M/2)])
                if front_part == back_part:
                    ans = box[i][j:j+M]
                

    # # 세로 탐색
    # for i in range(N):
    #     for j in range(N):
    #         print('')

    print(box)

    # print(f'#{test_case} {ans}')
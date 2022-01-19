n = open("SW Expert Academy\Programming Intermediate_Stack\input.txt", "r")

T = int(n.readline())

for test_case in range(1, T + 1):
    # 문자열 받기
    inputtext = n.readline().rstrip()

    # 텍스트 스택
    text_stack = []

    # 텍스트 하나씩 반복문
    for t in inputtext:
        
        # 스택이 비어있다면 push
        if not text_stack:
            text_stack.append(t)
            continue
        # 스택의 top과 추가할 문자가 같으면
        if text_stack[-1] == t:
            text_stack.pop() # 마지막 요소 pop
        else:
            text_stack.append(t) # 추가할 문자를 top으로
    
    ans = len(text_stack) # 최종 스택의 길이가 정답

    print(f'#{test_case} {ans}')
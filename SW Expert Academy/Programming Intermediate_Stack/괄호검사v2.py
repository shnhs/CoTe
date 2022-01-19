n = open("SW Expert Academy\Programming Intermediate_Stack\input.txt", "r")

T = int(n.readline())

for test_case in range(1, T + 1):
    # 문자열 받기
    Text = n.readline().rstrip()

    # 괄호 딕셔너리 선언
    bracket = {'(':')', '{':'}'}

    bracket_stack = []  # 괄호 스택 선언
    
    ans = 1 # 기본적으로 정답은 1
    # 문자열 하나씩 반복
    for b in Text:
        if b in bracket.keys():
            bracket_stack.append(b) # 여는괄호라면 스택에 push
        # 닫는괄호일때
        elif b in bracket.values():
            if not bracket_stack:
                ans = 0 # 여는괄호가 없는데 닫는괄호가 나오면 잘못됨
                break # for문 중단하고 빠져나감
            if bracket[bracket_stack.pop()] == b:
                pass # 만약 여는괄호와 닫는괄호가 매칭되면 pass
            else:
                ans = 0 # 매칭되지 않으면 잘못됨
                break
    
    # 문자열을 다 돌았는데 스택에 괄호가 남아있으면 잘못됨
    if len(bracket_stack) != 0:
        ans = 0

    print(f'#{test_case} {ans}')
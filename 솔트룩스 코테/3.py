def solution(encrypted_text, key, rotation):

    # abc 문자열 리스트 생성
    abc_list = []
    for x in range(97, 123):
        abc_list.append(chr(x))
    
    # T는 문자열 길이
    T = len(encrypted_text)
    if rotation > 0:
        # 앞의 rot % T 만큼 뒤로이동
        before_rot = encrypted_text[(rotation%T):] + encrypted_text[:(rotation%T)]
    else:
        # 뒤의 rot % T 만틈 앞으로 이동
        before_rot = encrypted_text[-(-rotation%T):] + encrypted_text[:-(-rotation%T)] 
    
    # 암호화 이전 문자열 인덱스 계산
    before_encrypted = []
    for i, j in zip(before_rot, key):
        before_encrypted.append((ord(i)-96) - (ord(j)-96))

    # 정답리스트 생성
    answer = []
    for i in before_encrypted:
        answer.append(abc_list[i-1])

    return "".join(answer)

print(solution("qyyigoptvfb","abcdefghijk",3))

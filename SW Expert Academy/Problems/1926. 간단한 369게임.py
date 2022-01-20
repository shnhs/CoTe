# N = int(input())

N=40

def gamex3(N):
    ans = []
    for i in range(1,N+1):
        temp = list(str(i))
        # 3,6,9의 갯수 카운팅
        cnt = temp.count('3') + temp.count('6') + temp.count('9')

        if cnt == 0: # 3,6,9가 없다면 pass
            ans.append(str(i))
        else: # 3,6,9가 있다면 카운트만큼 '-'
            ans.append('-'*cnt)
    
    return ' '.join(ans)

print(gamex3(N))
dict = {1: '가위', 2: '바위', 3: '보'}
while(1):
    play = int(input("가위(1), 바위(2), 보(3) 를 입력하세요: "))
    if (play > 3) or (play < 1):
        print("입력이 올바르지 않습니다.")
        continue
    else:
        break

com = int(random.randint(1,3))
print(f"플레이어 입력은 {dict[play]}입니다.")
print(f"컴퓨터는 {dict[com]}입니다.")

if com == play:
    print("무승부입니다.")
elif (com - play) == -1 or (com - play) == 2:
    print("승리입니다.")
else:
    print('패배입니다.')
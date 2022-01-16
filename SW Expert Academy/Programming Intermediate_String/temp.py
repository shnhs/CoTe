from math import ceil

# 'A','B','B','C','B','B','A'
N,M = 10, 7
# box = [['G', 'O', 'F', 'F', 'A', 'K', 'W', 'F', 'S', 'M'],
#          ['O', 'Y', 'E', 'C', 'R', 'S', 'L', 'D', 'L', 'Q'],
#          ['U', 'J', 'A', 'J', 'Q', 'V', 'S', 'Y', 'Y', 'C'],
#          ['J', 'A', 'E', 'Z', 'N', 'N', 'Z', 'E', 'A', 'J'],
#          ['W', 'J', 'A', 'K', 'C', 'G', 'S', 'G', 'C', 'F'],
#          ['Q', 'K', 'U', 'D', 'G', 'A', 'T', 'D', 'Q', 'L'],
#          ['O', 'K', 'G', 'P', 'F', 'P', 'Y', 'R', 'K', 'Q'],
#          ['T', 'D', 'C', 'X', 'B', 'M', 'Q', 'T', 'I', 'O'],
#          ['U', 'N', 'A', 'D', 'R', 'P', 'N', 'E', 'T', 'Z'],
#          ['Z', 'A', 'T', 'W', 'D', 'E', 'K', 'D', 'Q', 'F']]
box = [['G', 'O', 'F', 'F', 'A', 'K', 'W', 'F', 'S', 'M'],
       ['O', 'Y', 'E', 'C', 'R', 'S', 'L', 'D', 'L', 'Q'],
       ['U', 'J', 'A', 'J', 'Q', 'V', 'S', 'Y', 'Y', 'C'],
       ['J', 'A', 'E', 'Z', 'N', 'N', 'Z', 'E', 'A', 'J'],
       ['W', 'J', 'A', 'K', 'C', 'G', 'S', 'G', 'C', 'F'],
       ['Q', 'K', 'U', 'D', 'G', 'A', 'T', 'D', 'Q', 'L'],
       ['O', 'K', 'G', 'P', 'F', 'P', 'Y', 'R', 'K', 'Q'],
       ['A', 'B', 'B', 'C', 'B', 'B', 'A', 'T', 'I', 'O'],
       ['U', 'N', 'A', 'D', 'R', 'P', 'N', 'E', 'T', 'Z'],
       ['Z', 'A', 'T', 'W', 'D', 'E', 'K', 'D', 'Q', 'F']]
for i in range(N):
        for j in range(N):
            if M % 2 == 1:
                front_part = ''.join(reversed(box[i][j:j+int(M/2)]))
                back_part = ''.join(box[i][j+1+int(M/2):j+1+2*int(M/2)])
                # print(front_part, back_part)
                if front_part == back_part:
                    ans = box[i][j:j+M]
                    print(ans)


from audioop import reverse


# X = ['a', 'b', 'c']
# Y = list(reversed(X))
# print(Y)
# # print(''.join(X))
# print(''.join(Y))
# print( 'cba' == ''.join(Y))

'''
R과 L중 무엇이 더 많은지 측정
기각:
RRRRLLLLRLLRL
L이 7개 R이 6개 임에도 불구하고 R방향으로 4가 정답

50개를 전부 dfs로?
기각: 2^50 불가

가지치기가 가능한가?
기각:

?에 전부다 R 넣고 전부다 L넣는 경우만 확인하면 되나???
된다!

'''

def solution(S):
    left= 0
    right= 0

    current= 0
    for i in range(len(S)): # ?==L
        if(S[i]=="R"):
            current+=1
        else:
            current-=1
        # print(S[i], current)
        if(left<abs(current)):
            left= abs(current)

    # print()
    # print()

    current= 0
    for i in range(len(S)): # ?==R
        if(S[i]=="L"):
            current-=1
        else:
            current+=1
        # print(S[i], current)
        if(right<abs(current)):
            right= abs(current)

    return max(left, right)


## main ##
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    S= input()
    print(solution(S))
# S= "LLRR"
# print(solution(S))
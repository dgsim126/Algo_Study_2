'''
최빈수 구하기
가장 많이 나타나는 점수를 구하라(여러 개일때는 큰 점수)
점수 범위 0 ~ 100
학생 수 1000
'''
def solution(scores):
    lst= [0]*1001 # 0~1000

    for i in range(len(scores)): # 0~999
        current_score= scores[i]
        lst[current_score]+=1

    max_score= max(lst)

    for i in range(len(lst)-1, -1, -1): # 1000~0
        if(lst[i]==max_score):
            return i

## main ##
T = int(input())
for test_case in range(1, T + 1):
    input()
    scores= list(map(int, input().split()))
    print(f"#{test_case} {solution(scores)}")

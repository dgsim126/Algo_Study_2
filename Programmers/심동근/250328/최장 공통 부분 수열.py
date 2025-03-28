'''
문자열의 길이의 최대는 1000, 4초의 시간을 주기에 단순하게 접근해도 될 것 같다.

dfs? 근데 그냥 collections로 해도 될 듯. 둘 다 시간초과 예상 DP문제?

두 단어 중 작은 값의 길이를 기준으로 조합을 생성
생성된 각 조합들이 긴 단어에 포함되는지 확인
포함안되면 길이 하나 줄이고 조합 다시 생성
반복

-- worst case 문자열 1000개 두 개가 주어지고, 겹치는게 1개 길이의 문자열일 때 4억번 연산안에 불가능.
일단 진행? ========>>>>>>>>> 제한시간 초과
'''
from itertools import combinations
from collections import deque

def check(short, long):
    remind= short
    short= deque(short)
    long= deque(long)

    '''
    short에서 값을 하나 뺀다.
    long에서 short에 해당하는 값이 나올때까지 뺀다.
    같은 값이 나오면 short는 다음 값을 뺀다
    
    long이 다 사라졌는데 short에 값이 남았다면 return 0
    short가 다 사라졌다면 return len(short)
    '''

    while(True):
        current_short= short.popleft()
        while(True):
            if(len(long)==0):
                return 0
            current_long= long.popleft()
            if(current_short==current_long):
                break
        if(len(short)==0):
            return len(remind)


def solution(word1, word2):
    short= "0"
    long= "0"
    if(len(word1)>len(word2)):
        short= word2
        long= word1
    else:
        short= word1
        long= word2

    for i in range(len(short), 0, -1):
        for comb in combinations(short, i):

            result= check(list(comb), long)

            if(result!=0):
                return len(comb)

## main ##
T = int(input())
for test_case in range(1, T + 1):
    word1, word2= input().split()
    print(f"#{test_case} {solution(word1, word2)}")

# word1= "abcdefgg"
# word2= "abcdefegeeg"
# print(solution(word1, word2))
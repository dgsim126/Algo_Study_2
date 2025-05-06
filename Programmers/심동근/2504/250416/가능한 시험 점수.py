'''
제한시간 초과 발생


'''

# from itertools import combinations
#
# def solution(N, score):
#     result= set()
#     result.add(0)
#
#     for i in range(1, N+1):
#         for comb in combinations(score, i):
#             result.add(sum(comb))
#
#     return len(result)

'''
max_score 사이즈만큼의 dp 리스트를 만들고 전부 False로 초기화한 다음,

'''

#gpt
def solution(N, scores):
    max_score = sum(scores)
    dp = [False] * (max_score + 1)
    dp[0] = True  # 0점은 항상 가능 (아무것도 선택 안했을 때)

    for score in scores:
        # 뒤에서부터 돌려야 중복 계산 방지 (score가 여러 번 더해지지 않게)
        for i in range(max_score, -1, -1):
            if dp[i]:
                dp[i + score] = True

    return sum(dp)  # True인 개수가 만들 수 있는 점수의 개수

# Main
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    print(f"#{test_case} {solution(N, scores)}")




## main ##
T = int(input())
for test_case in range(1, T + 1):
    N= int(input())
    score= list(map(int, input().split()))
    print(f"#{test_case} {solution(N, score)}")
# N= 1 # 문제의 개수
# score= [1]
# print(solution(N, score))
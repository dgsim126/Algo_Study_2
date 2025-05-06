'''
dfs로 풀어야 하는 문제로 보인다.
dfs로 모든 조합을 확인하며 내려가고 칼로리를 초과하는 경우 return 시키면 된다.
이때 최대값을 구하면 된다.
'''

def solution(N, max_kcal, score, kcal):
    def dfs(depth, current_score, current_kcal):
        global max_score

        if(current_kcal > max_kcal):
            return

        max_score = max(max_score, current_score)

        # 재료를 하나씩 선택하여 재귀 호출
        for i in range(depth, N):
            if(is_visited[i]==False):
                is_visited[i]= True

                dfs(depth+1, current_score+score[i], current_kcal+kcal[i])

                is_visited[i]= False

    global max_score
    max_score= 0
    is_visited = [False] * N
    dfs(0, 0, 0)

    return max_score

## main ##
T = int(input())  # 테스트 케이스 개수

# 여러 개의 테스트 케이스 처리
for test_case in range(1, T + 1):
    N, L = map(int, input().split())  # N: 재료 개수, L: 최대 칼로리

    # 맛 점수와 칼로리를 저장할 리스트
    s = []
    k = []

    # N개의 줄에서 (맛 점수, 칼로리) 입력 받기
    for _ in range(N):
        score, kcal = map(int, input().split())
        s.append(score)
        k.append(kcal)

    # solution 함수 실행
    max_taste = solution(N, L, s, k)

    # 결과 출력 (테스트 케이스 번호 포함)
    print(f'#{test_case} {max_taste}')



## main ##
# N = 5  # 재료의 수
# max_kcal = 1000  # 섭취가능한 칼로리
# score = [100, 300, 250, 500, 400]  # 재료별 맛 점수
# kcal = [200, 500, 300, 1000, 400]  # 재료별 칼로리
#
# print(solution(N, max_kcal, score, kcal))  # 최대 점수 출력

#=====================================================================================================================
def solution(N, max_kcal, score, kcal):
    def dfs(i, current_score, current_kcal):
        global max_score

        # 칼로리 초과하면 탐색 중단 (가지치기)
        if current_kcal > max_kcal:
            return

        # 최대 점수 갱신
        max_score = max(max_score, current_score)

        # 모든 재료를 탐색한 경우 종료
        if i == N:
            return

        # 현재 재료 선택
        dfs(i + 1, current_score + score[i], current_kcal + kcal[i])

        # 현재 재료 선택 안 함
        dfs(i + 1, current_score, current_kcal)

    global max_score
    max_score = 0
    dfs(0, 0, 0)

    return max_score


## main ##
T = int(input())  # 테스트 케이스 개수

# 여러 개의 테스트 케이스 처리
for test_case in range(1, T + 1):
    N, L = map(int, input().split())  # N: 재료 개수, L: 최대 칼로리

    # 맛 점수와 칼로리를 저장할 리스트
    s = []
    k = []

    # N개의 줄에서 (맛 점수, 칼로리) 입력 받기
    for _ in range(N):
        score, kcal = map(int, input().split())
        s.append(score)
        k.append(kcal)

    # solution 함수 실행
    max_taste = solution(N, L, s, k)

    # 결과 출력 (테스트 케이스 번호 포함)
    print(f'#{test_case} {max_taste}')

'''
dfs(0, 0, 0)
├── dfs(1, 100, 200)  → 첫 번째 재료 선택
│   ├── dfs(2, 300, 500) → 두 번째 재료 선택
│   │   ├── dfs(3, 600, 900) → 세 번째 재료 선택 (칼로리 초과) ❌ 가지치기
│   │   ├── dfs(3, 300, 500) → 세 번째 재료 선택 안 함 ✅
│   ├── dfs(2, 100, 200) → 두 번째 재료 선택 안 함
│       ├── dfs(3, 400, 600) → 세 번째 재료 선택 (칼로리 초과) ❌ 가지치기
│       ├── dfs(3, 100, 200) → 세 번째 재료 선택 안 함 ✅
├── dfs(1, 0, 0) → 첫 번째 재료 선택 안 함
│   ├── dfs(2, 200, 300) → 두 번째 재료 선택
│   │   ├── dfs(3, 500, 700) → 세 번째 재료 선택 (칼로리 초과) ❌ 가지치기
│   │   ├── dfs(3, 200, 300) → 세 번째 재료 선택 안 함 ✅
│   ├── dfs(2, 0, 0) → 두 번째 재료 선택 안 함
│       ├── dfs(3, 300, 400) → 세 번째 재료 선택 ✅
│       ├── dfs(3, 0, 0) → 세 번째 재료 선택 안 함 ✅

'''



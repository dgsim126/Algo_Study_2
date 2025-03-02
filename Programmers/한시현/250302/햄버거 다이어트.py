T = int(input())

def dfs(idx, total_score, total_calorie):
    global max_score # global : 함수 내에서 전역 변수 수정 가능

    if total_calorie > L:
        return

    max_score = max(max_score, total_score) # 약간 빠름
    # if total_score > max_score:
    #     max_score = total_score

    if idx == N:
        return

    # 재료 선택 o, 재귀
    dfs(idx + 1, total_score + taste_score[idx], total_calorie + calories[idx])
    # 재료 선택 x, 재귀
    dfs(idx + 1, total_score, total_calorie)

for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    taste_score = []
    calories = []

    for _ in range(N):
        t_s, c = map(int, input().split())
        taste_score.append(t_s)
        calories.append(c)

    max_score = 0

    dfs(0,0,0)

    print(f'#{test_case} {max_score}')
def solution(N, buildings):
    answer = 0
    for i in range(2, N-2):
        max_ = max((buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]))
        if max_ >= buildings[i]:
            continue
        else:
            answer += buildings[i] - max_
    return answer

for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    answer = solution(N, buildings)

    print(f"#{test_case} {answer}")
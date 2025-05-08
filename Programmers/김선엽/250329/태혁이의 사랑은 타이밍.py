def solution(D, H, M):
    meeting = (11 * 24 * 60) + (11 * 60) + 11
    realize = (D * 24 * 60) + (H * 60) + M

    if realize < meeting:
        return -1
    else:
        return realize - meeting
    
T = int(input())
for test_case in range(1, T+1):
    D, H, M = map(int, input().split())
    answer = solution(D, H, M)

    print(f"#{test_case} {answer}")
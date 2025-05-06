def who_win(first, second):
    # 1: 가위, 2: 바위, 3: 보
    if first == second:
        return 0
    elif (first == 1 and second == 3) or (first == 2 and second == 1) or (first == 3 and second == 2):
        return 0
    else:
        return 1


def tournament(lst, start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    left = tournament(lst, start, mid)
    right = tournament(lst, mid + 1, end)
    if who_win(lst[left], lst[right]) == 0:
        return left
    else:
        return right


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    winner_idx = tournament(lst, 0, N - 1)
    print(f"#{test_case} {winner_idx + 1}")
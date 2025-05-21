from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort(reverse=True)
    w = deque(w)
    t.sort(reverse=True)

    total = 0
    for truck in t:
        while w:
            con = w.popleft()
            if truck >= con:
                total += con
                break
        if not w:
            break

    print(f'#{test_case} {total}')
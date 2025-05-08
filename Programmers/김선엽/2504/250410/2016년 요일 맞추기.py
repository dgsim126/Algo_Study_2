def solution(m, d):
    calendar = {
        1 : 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    date = {
        0: 4,
        1: 5,
        2: 6,
        3: 0,
        4: 1,
        5: 2,
        6: 3
    }

    day = 0
    if m > 1:
        for i in range(1, m):
            day += calendar[i]
    day += d - 1

    return date[day%7]

T = int(input())
for test_case in range(1, T+1):
    m, d = map(int, input().split())
    answer = solution(m, d)
    print(f"#{test_case} {answer}")
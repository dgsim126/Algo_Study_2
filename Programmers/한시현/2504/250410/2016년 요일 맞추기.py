T = int(input())
for test_case in range(1, T + 1):
    m, d = map(int, input().split())
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = {
        '0': 4, # 금
        '1': 5, # 토
        '2': 6, # 일
        '3': 0, # 월
        '4': 1, # 화
        '5': 2, # 수
        '6': 3, # 목
    }
    total = sum(months[:m-1]) + d-1
    current = total % 7

    print(f'#{test_case} {days[str(current)]}')
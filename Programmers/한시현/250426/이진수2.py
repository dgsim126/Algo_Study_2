T = int(input())
for test_case in range(1, T + 1):
    N = float(input())
    result = ''
    count = 0

    while N != 0:
        count += 1
        if count > 12:
            result = 'overflow'
            break

        N *= 2
        if N >= 1: # 정수가 생기면 1
            result += '1'
            N -= 1
        else: # 정수 안 생기면 0
            result += '0'

    print(f"#{test_case} {result}")
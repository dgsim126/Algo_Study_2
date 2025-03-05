T = 10
for test_case in range(1, T + 1):
    n = int(input())
    table = []
    for i in range(n):
        line = list(map(int, input().split()))
        table.append(line)

    count = 0
    for col in range(n):
        meet = []
        for row in range(n):
            if table[row][col] == 1: # N극 (테이블 아래로 이동)
                meet.append(1)
            elif table[row][col] == 2:  # S극 (테이블 위로 이동)
                if meet:
                    meet.pop()
                    count += 1

    print(f'#{test_case} {count}')


T = 10
for test_case in range(1, T + 1):
    n = int(input())
    table = []
    for i in range(n):
        line = list(map(int, input().split()))
        table.append(line)

    count = 0
    for col in range(n):
        N_exist = False
        for row in range(n):
            if table[row][col] == 1: # N극 (테이블 아래로 이동)
                N_exist = True
            elif table[row][col] == 2:  # S극 (테이블 위로 이동)
                if N_exist:
                    count += 1
                    N_exist = False

    print(f'#{test_case} {count}')
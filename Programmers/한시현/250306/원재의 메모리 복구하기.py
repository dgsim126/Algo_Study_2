# 초기화 상태 : 모든 bit가 0
T = int(input())
for test_case in range(1, T + 1):
    memory = input()
    memory_list = [n for n in memory]

    count = 0
    status = False # True = 1, False = 0
    for bit in memory_list:
        if bit == '1' and not status: # 원본 1, 현재 0
            status = True
            count += 1

        elif bit == '0' and status: # 원본 0, 현재 1
            status = False
            count += 1

    print(f'#{test_case} {count}')
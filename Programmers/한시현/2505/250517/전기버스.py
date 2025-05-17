T = int(input())
for test_case in range(1, T + 1):
    move, goal, station_num = map(int, input().split())
    stations = set(map(int, input().split())) # in 탐색은 set이 훨씬 빠른것 잊지 말자

    current = 0
    count = 0
    while current+move < goal:
        find = False
        for i in range(current+move, current, -1):
            if i in stations:
                find = True
                current = i
                count += 1
                break
        if not find:
            count = 0
            break

    print(f'#{test_case} {count}')
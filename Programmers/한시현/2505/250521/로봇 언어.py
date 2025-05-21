T = int(input())
for test_case in range(1, T + 1):
    commands = list(input().strip())
    recent = 0
    l = commands.count('L')
    r = commands.count('R')
    if l > r:
        case = 1
    else:
        case = 2

    for cmd in commands:
        if cmd == 'R':
            recent += 1
        elif cmd == 'L':
            recent -= 1
        elif cmd == '?':
            if case == 1:
                recent -= 1
            else:
                recent += 1

    print(f'{abs(recent)}')
    # print(f'#{test_case} {abs(recent)}') # 2트.. 진짜 조심
    # 왜 틀림?
    # 원점에서부터 가장 멀리 떨어진 순간의 거리를 구해야한다.


T = int(input())
for test_case in range(1, T + 1):
    commands = list(input().strip())
    recent1 = 0
    recent2 = 0
    case = []

    for cmd in commands:
        if cmd == 'R':
            recent1 += 1
            recent2 += 1
            case.append(abs(recent1))
            case.append(abs(recent2))
        elif cmd == 'L':
            recent1 -= 1
            recent2 -= 1
            case.append(abs(recent1))
            case.append(abs(recent2))
        elif cmd == '?':
            recent1 += 1
            case.append(abs(recent1))
            recent2 -= 1
            case.append(abs(recent2))

    print(f'{max(case)}')
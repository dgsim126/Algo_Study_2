for test_case in range(1, 11):
    n = int(input())
    pw = list(map(int, input().split()))
    cmd_num = int(input())
    cmd = input().split()

    i = 0
    while i < len(cmd):
        ist = []
        if cmd[i] == 'I':
            i += 1
            idx = int(cmd[i])
            i += 1
            quan = int(cmd[i])
            i += 1
            for _ in range(quan):
                ist.append(cmd[i])
                i += 1

            pw[idx:idx] = list(map(int, ist))

    answer = pw[:10]
    print(f'#{test_case}', *answer)
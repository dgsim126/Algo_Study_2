# 다양한 시도 연습
for test_case in range(1, 11):
    n = int(input())
    pw = list(map(int, input().split()))
    cmd_num = int(input())
    cmd = input().split()

    i = 0
    while i < len(cmd):
        lst = []

        if cmd[i] == 'I':
            i += 1
            idx = int(cmd[i])
            i += 1
            count = int(cmd[i])
            i += 1
            for _ in range(count):
                lst.append(int(cmd[i]))
                i += 1

            pw[idx:idx] = lst

        elif cmd[i] == 'D':
            i += 1
            start = int(cmd[i])
            i += 1
            end = start + int(cmd[i])
            i += 1

            # try 1.
            # del pw[start:end]

            # try 2.
            pw[start:end] = []

        else: # cmd[i] == 'A'
            i += 1
            count2 = int(cmd[i])
            i += 1

            # try 1.
            # for _ in range(count2):
            #     pw.append(int(cmd[i]))
            #     i += 1

            # try 2.
            save = []
            for _ in range(count2):
                save.append(int(cmd[i]))
            pw.extend(save)
            i += count2

    answer = pw[:10]
    print(f'#{test_case}', *answer)
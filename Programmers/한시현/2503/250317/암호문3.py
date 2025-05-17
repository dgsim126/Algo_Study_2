T = 10
for test_case in range(1, T + 1):
    pw_len = int(input())
    pw = input().split()
    command_num = int(input())
    command = input().split('I ')[1:]

    for cmd in command:
        cmd = cmd.split()
        if cmd[0] == 'D':
            del pw[int(cmd[1]):int(cmd[1])+int(cmd[2])] # pw[cmd[1]:cmd[1]+cmd[2]] = []

        elif cmd[0] == 'A':
            pw += cmd[2:]

        else: # I를 기준으로 분할했으므로 idx 0 에 명령어 없이 시작
            pw[int(cmd[0]):int(cmd[0])] = cmd[2:]

    print(f"#{test_case} {' '.join(pw[:10])}")
from collections import deque

T = 10
for test_case in range(1, T + 1):
    pw_len = int(input())
    pw = input().split()
    command_num = int(input())
    command = input().split('I ')[1:] # 'I ' 앞 뒤로 나누기 때문에 I로 시작하면 앞에 공백이 생긴다.

    for cmd in command:
        cmd_list = deque(cmd.split())
        location = cmd_list.popleft()
        add_num = cmd_list.popleft()

        cmd_list.reverse()
        for i in cmd_list:
            pw.insert(int(location), i) # 더 좋은 방법 : pw[x:x] = s(리스트)

    str_pw = ' '.join(pw[:10])

    print(f"#{test_case} {str_pw}")
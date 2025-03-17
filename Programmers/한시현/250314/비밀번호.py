T = 10
for test_case in range(1, T + 1):
    n, p = map(int, input().split())
    pw = list(str(p))

    check_list = []
    for pw_i in pw:
        if check_list and check_list[-1] == pw_i:
            check_list.pop()
        else:
            check_list.append(pw_i)

    pw_int = int("".join(check_list))

    print(f"#{test_case} {pw_int}")
T = int(input())
for test_case in range(1, T + 1):
    s = input()
    s_count = s.count('o')
    left = 15-len(s)

    if s_count + left >= 8:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')
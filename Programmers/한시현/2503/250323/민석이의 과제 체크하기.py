T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    stud_num = list(map(int, input().split()))

    all_stud = []
    for i in range(1, n+1):
        if i not in stud_num:
            all_stud.append(i)

    answer = " ".join(map(str, all_stud))

    print(f'#{test_case} {answer}')
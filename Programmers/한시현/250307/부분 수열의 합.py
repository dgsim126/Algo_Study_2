T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    count = 0
    for i in range(len(num_list)-1):
        if i == len(num_list) - 1:
            if i + 1 == K:
                count += 1
            break

        add = num_list[i]
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == K:
                count += 1
                print(f'{num_list[i]}, {num_list[j]} case1')
            if add == K:
                count += 1
                print(f'{num_list[i]}, {num_list[j]} case2')
                break
            add += num_list[j]
            if add > K:
                break

    print(f'#{test_case} {count}')
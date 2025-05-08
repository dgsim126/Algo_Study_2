T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N 정점, M 간선
    print(f'{N}, {M}')
    for i in range(M):
        x, y = map(int, input().split())
        print(f'{x}, {y}')

    print('skip')
    #print(f'#{test_case} {count}')
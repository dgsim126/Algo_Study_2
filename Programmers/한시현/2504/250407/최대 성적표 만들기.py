T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse = True)
    answer = scores[0:k]

    print(f'#{test_case} {sum(answer)}')
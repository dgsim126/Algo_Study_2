T = int(input())
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())

    if b*2 == a+c:
        print(f'#{test_case} 0.0') # ㅋㅋ
    else:
        print(f'#{test_case} {abs(b - (a+c)/2)}')
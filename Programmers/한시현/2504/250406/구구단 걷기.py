T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    x_list = [0, 0]
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if x_list[0] < i:
                x_list = [i, n//i]

    print(f'#{test_case} {x_list[0]-1 + x_list[1]-1}') # 출력문 형태 신경쓰자..
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    table = []
    for i in range(8):
        table.append(input())

    count = 0

    # 가로 탐색
    for row in range(8):
        for start in range(8):
            end = start + n
            if end > 8:
                continue

            word = table[row][start:end]
            if word == word[::-1]:
                count += 1

    # 세로 탐색
    for col in range(8):
        for start in range(8):
            end = start + n
            if end > 8:
                continue

            word = # start 부터 n 길이의 세로로 위치한 문자들을 word 에 넣고 문자열 만들기
            if word == word[::-1]:
                count += 1

    print(f'#{test_case} {count}')
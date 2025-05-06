for test_case in range(1, 11):
    n = int(input())
    board = [input() for _ in range(8)]

    count = 0
    # 가로
    for i in range(8):
        for j in range(8-n+1):
            word1 = board[i][j:j+n]
            if word1 == word1[::-1]:
                count += 1

    # 세로
    for col in range(8):
        for row in range(8-n+1):
            word_list = []
            for i in range(n):
                word_list.append(board[row+i][col])
            word2 = ''.join(word_list)
            if word2 == word2[::-1]:
                count += 1

    print(f'#{test_case} {count}')
for test_case in range(1, 11):
    tc = int(input())
    board = [input() for _ in range(100)]

    gotcha = 0
    for p_len in range(100, 0, -1):
        # 가로
        for y in range(100):
            for x in range(100-p_len+1):
                word1 = board[y][x:x+p_len]
                if word1 == word1[::-1]:
                    gotcha = p_len
                    break
            if gotcha != 0:
                break
        if gotcha != 0:
            break

        # 세로
        for row in range(100):
            for col in range(100-p_len+1):
                lst = []
                for c in range(p_len):
                    lst.append(board[col+c][row])
                word2 = ''.join(lst)
                if word2 == word2[::-1]:
                    gotcha = p_len
                    break
            if gotcha != 0:
                break
        if gotcha != 0:
            break

    print(f'#{tc} {gotcha}')

    # 댓글)
    # 문제가 이상합니다. 아래 댓글보고 고쳤어요.
    # tc 번호를 입력받은 번호를 안쓰고 for문 돌린 번호를 이용하면 오답이 나옵니다.
    # 뭐 이런경우가 있는지;;
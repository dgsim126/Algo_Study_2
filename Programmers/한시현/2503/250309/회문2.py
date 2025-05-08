T = 10
for test_case in range(1, T + 1):
    def find_max_palindrome(board):
        max_length = 1  # 최소 회문 길이

        # 가로 방향 및 세로 방향 검사
        for length in range(2, 101):  # 길이 2부터 100까지 가능한 회문 확인
            for i in range(100):  # 행과 열을 돌면서 검사
                for start in range(101 - length):  # 시작 위치 조정
                    # 가로 방향 확인
                    row_substring = board[i][start:start + length]
                    if row_substring == row_substring[::-1]:
                        max_length = max(max_length, length)

                    # 세로 방향 확인 (리스트에서 하나씩 문자 조합)
                    col_substring = ''.join(board[row][i] for row in range(start, start + length))
                    if col_substring == col_substring[::-1]:
                        max_length = max(max_length, length)

        return max_length


    # 테스트 케이스 실행
    for _ in range(10):
        board = [input().strip() for _ in range(100)]  # 100x100 글자판 입력

        result = find_max_palindrome(board)
        print(f"#{test_case} {result}")
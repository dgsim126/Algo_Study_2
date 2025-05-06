# def solution(palindrome):
#     max_ = 0
#     is_pal = False
#     for i in range(200):
#         for j in range(100, 2, -1):
#             for k in range(0, 101 - j):
#                 if palindrome[i][k:k+j] == palindrome[i][k:k+j][::-1]:
#                     is_pal = True
#                     max_ = max(max_, j)
#                     break
#
# for test_case in range(10):
#     T = int(input())
#     palindrome= []
#     for i in range(100):
#         row_ = list(input())
#         palindrome.append(row_)
#         col_ = []
#         for j in range(100):
#             col_.append(row_[j][i])
#         palindrome.append(col_)
#
#     answer = solution(palindrome)
#
#     print(f"#{test_case} {answer}")

def is_palindrome(s):
    return s == s[::-1]

for _ in range(10):
    tc = int(input())
    board = [input() for _ in range(100)]
    max_len = 0

    for row in board:
        for length in range(100, 0, -1):
            if max_len >= length:
                break
            for start in range(101 - length):
                if is_palindrome(row[start:start+length]):
                    max_len = length
                    break

    for col in range(100):
        for length in range(100, 0, -1):
            if max_len >= length:
                break
            for start in range(101 - length):
                temp = "".join([board[start+i][col] for i in range(length)])
                if is_palindrome(temp):
                    max_len = length
                    break

    print(f"#{tc} {max_len}")
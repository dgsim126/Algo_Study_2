def solution(n, board):
    answer = 0
    loop_len = 8 - n
    a = n // 2

    for i in range(8):
        for j in range(8):
            if j <= loop_len:
                row_list = board[i][j:j+n]
                if row_list == row_list[::-1]:
                    answer += 1
            
            list = []
            if i <= loop_len:
                for k in range(i, i+n):
                    list.append(board[k][j])
                
                if list == list[::-1]:
                    answer += 1
    
    return answer


# board = [
#     ['C', 'B', 'B', 'C', 'B', 'A', 'A', 'B'],
#     ['C', 'C', 'C', 'B', 'A', 'B', 'C', 'B'],
#     ['C', 'A', 'A', 'A', 'A', 'C', 'A', 'B'],
#     ['B', 'A', 'C', 'C', 'C', 'C', 'A', 'C'],
#     ['A', 'A', 'B', 'C', 'B', 'B', 'A', 'C'],
#     ['A', 'C', 'A', 'A', 'C', 'A', 'B', 'C'],
#     ['B', 'C', 'C', 'B', 'A', 'A', 'B', 'C'],
#     ['A', 'B', 'B', 'B', 'C', 'C', 'A', 'A']
# ]

board = [
    ['B', 'C', 'B', 'B', 'C', 'A', 'C', 'A'],
    ['B', 'C', 'A', 'A', 'A', 'C', 'A', 'C'],
    ['A', 'B', 'A', 'C', 'B', 'C', 'C', 'B'],
    ['A', 'A', 'C', 'B', 'C', 'B', 'C', 'A'],
    ['A', 'C', 'A', 'C', 'B', 'A', 'A', 'A'],
    ['A', 'C', 'C', 'A', 'C', 'C', 'C', 'B'],
    ['A', 'A', 'C', 'A', 'A', 'A', 'B', 'A'],
    ['C', 'A', 'C', 'C', 'A', 'B', 'C', 'B']
]

print(solution(4, board))
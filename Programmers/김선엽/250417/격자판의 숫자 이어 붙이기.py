from collections import deque

def solution(board):
    queue = deque([])
    for i in range(4):
        for j in range(4):
            queue.append([i, j, 0, board[i][j]])

    numbers = set()
    
    direction = ([-1, 0], [1, 0], [0, -1], [0, 1])

    while queue:
        x, y, t, cur = queue.popleft()

        if t < 6:
            for dx, dy in direction:
                rx, ry = x + dx, y + dy
                if 0 <= rx < 4 and 0 <= ry < 4:
                    queue.append([rx, ry, t+1, cur+board[rx][ry]])
        else:
            numbers.add(cur)

    return len(numbers)

T = int(input())
for test_case in range(1, T+1):
    board = []
    for _ in range(4):
        board.append(list(map(str, input().split())))

    answer = solution(board)

    print(f"#{test_case} {answer}")
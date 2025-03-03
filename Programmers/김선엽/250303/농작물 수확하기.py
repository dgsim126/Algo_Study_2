# 풀이

def solution(n, farm):
    harvest = 0
    last = n - 1
    middle = (len(farm[0]) - 1) // 2
    for i in range(n):
        if i <= middle:
            for j in range(middle - i, middle + i + 1, 1):
                harvest += farm[i][j]
        else:
            for j in range(middle - (last - i), middle + (last - i) + 1, 1):
                harvest += farm[i][j]

        print(harvest)

    return harvest


farm = [
    [1, 4, 0, 5, 4],
    [4, 4, 2, 5, 0],
    [0, 2, 0, 3, 2],
    [5, 1, 2, 0, 4],
    [5, 2, 2, 1, 2]
]

print(solution(5, farm))


# 답안


def solution(n, farm):
    harvest = 0
    last = n - 1
    middle = (len(farm[0]) - 1) // 2
    for i in range(n):
        if i <= middle:
            for j in range(middle - i, middle + i + 1, 1):
                harvest += farm[i][j]
        else:
            for j in range(middle - (last - i), middle + (last - i) + 1, 1):
                harvest += farm[i][j]

        print(harvest)

    return harvest


farm = [
    [1, 4, 0, 5, 4],
    [4, 4, 2, 5, 0],
    [0, 2, 0, 3, 2],
    [5, 1, 2, 0, 4],
    [5, 2, 2, 1, 2]
]

print(solution(5, farm))
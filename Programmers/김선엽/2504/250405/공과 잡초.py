def solution(field):
    min = 0
    for i in range(len(field)):
        if field[i] == "(":
            if field[i+1] == "|" or field[i+1] == ")":
                min += 1
        if field[i] == ")" and field[i-1] == "|":
            min += 1
    
    return min

T = int(input())
for test_case in range(1, T+1):
    field = list(input())
    answer = solution(field)

    print(f"#{test_case} {answer}")
def solution(current):
    num_o = 0
    num_x = 0
    length = len(current)
    chance = 15 - length

    for i in range(length):
        if current[i] == "x":
            num_x += 1
        else:
            num_o += 1
    
    if (num_o + chance) >= 8:
        return "YES"
    else:
        return "NO"
    
T = int(input())
for test_case in range(1, T+1):
    current = input()
    answer = solution(current)

    print(f"#{test_case} {answer}")
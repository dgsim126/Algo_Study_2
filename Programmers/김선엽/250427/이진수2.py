def solution(number):
    index = -1
    result = ""
    while number > 0:
        # print(number)
        cur = number // 2**(index)
        if cur >= 1:
            result += "1"
            number -= cur * 2**(index)
        else:
            result += "0"

        index -= 1
    
    if len(result) >= 13:
        return "overflow"
    else:
        return result

# print(solution(0.625))
# print(solution(0.1))
# print(solution(0.125))

T = int(input())
for test_case in range(1, T+1):
    number = float(input())
    answer = solution(number)

    print(f"#{test_case} {answer}")
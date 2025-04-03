def solution(string):
    answer = 0
    start = ord("a")
    length = len(string)
    index = 0
    while index < length:
        cur = ord(string[index])
        if start == cur:
            answer += 1
        else:
            break
        start += 1
        index += 1
    
    return answer

# print(solution("abcdefghijklmnopqrstu"))
# print(solution("abcdefghijklmnopqrstuvwzyx"))
# print(solution("abcefghijk"))
# print(solution("xyz"))
# print(solution("absolute"))

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    answer = solution(string)

    print(f"#{test_case} {answer}")
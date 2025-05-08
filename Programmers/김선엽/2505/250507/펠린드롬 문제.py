## 짝수개 => 데칼코마니 짝 사용
## 홀수개 => 데칼코마니 짝, 가운데 펠린드롬

def solution(N, M, strings):
    palindrome = set(strings)
    # print(palindrome)
    is_reverse = 0
    is_palindrome = 0
    for string in strings:
        reverse_str = string[::-1]
        if reverse_str in palindrome and string != reverse_str: ## 데칼코마니 존재 O, 펠린드롬 X
            is_reverse += 1
        elif string == reverse_str: ## 펠린드롬 O => 같은건 존재 하지 않으므로 데칼코마니 X
            is_palindrome += 1

    # print(is_reverse, is_palindrome)

    if is_reverse == 0 and is_palindrome > 0:
        return M
    elif is_reverse > 0 and is_palindrome == 0:
        return is_reverse * M
    elif is_reverse > 0 and is_palindrome > 0:
        return (is_reverse + 1) * M
    else:
        return 0

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    strings = []
    for _ in range(N):
        strings.append(input())
    # print(strings)
    answer = solution(N, M, strings)

    print(f"#{test_case} {answer}")
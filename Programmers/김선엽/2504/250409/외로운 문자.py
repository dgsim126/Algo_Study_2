def solution(string):
    str_set = set()
    for i in range(len(string)):
        if string[i] in str_set:
            str_set.remove(string[i])
        else:
            str_set.add(string[i])
    if not str_set:
        return "Good"
    
    str_list = sorted(list(str_set))

    return "".join(str_list)

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    answer = solution(string)

    print(f"#{test_case} {answer}")
def solution(obj, string):
    answer = 0
    n = len(obj)
    m = len(string)

    for i in range(m-n+1):
        if string[i] == obj[0]:
            if string[i:i+n] == obj:
                answer += 1

    return answer

for test_case in range(10):
    T = int(input())
    obj = input()
    string = input()

    answer = solution(obj, string)

    print(f"#{T} {answer}")
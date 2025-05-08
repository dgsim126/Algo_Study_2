T = int(input())
for test_case in range(1, T + 1):
    sentence = list(input())
    check = []
    answer = 1

    for s in sentence:
        if s == '(' or s == '{':
            check.append(s)
        elif s == ')':
            if not check or check.pop() != '(':
                answer = 0
                break
        elif s == '}':
            if not check or check.pop() != '{':
                answer = 0
                break

    if check:
        answer = 0
    print(f'#{test_case} {answer}')
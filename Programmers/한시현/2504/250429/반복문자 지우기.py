T = int(input())
for test_case in range(1, T + 1):
    word = list(input().strip())
    answer = []
    for w in word:
        if not answer:
            answer.append(w)
        else:
            if answer[-1] != w:
                answer.append(w)
            elif answer[-1] == w:
                answer.pop()

    print(f"#{test_case} {len(answer)}")
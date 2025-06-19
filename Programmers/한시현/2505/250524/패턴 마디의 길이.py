T = int(input())
for test_case in range(1, T + 1):
    s = input()
    save = []
    answer = 0
    for i in range(len(s)):
        if save and s[i] == save[0]:
            if ''.join(save) == s[len(save):len(save)+len(save)]:
                answer = len(''.join(save))
                break
        save.append(s[i])

    print(f'#{test_case} {answer}')
T = int(input())
for test_case in range(1, T + 1):
    word = list(input())
    mo = 'aeiou'
    c_word = word.copy()

    for al in word:
        if al in mo:
            c_word.remove(al)
    answer = ''.join(c_word)

    print(f'#{test_case} {answer}')
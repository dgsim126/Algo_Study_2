T = int(input())
for test_case in range(1, T + 1):
    word = input()
    compare_word = input()

    answer = 0
    for i in range(len(compare_word)-len(word)+1):
        if compare_word[i:i+len(word)] == word:
            answer = 1
            break

    print(f'#{test_case} {answer}')
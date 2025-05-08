for test_case in range(1, 11):
    tc = int(input())
    word = input()
    sentence = input()

    count = 0
    for i in range(len(sentence)):
        if sentence[i] == word[0]:
            if sentence[i:i+len(word)] == word:
                count += 1

    print(f'#{test_case} {count}')
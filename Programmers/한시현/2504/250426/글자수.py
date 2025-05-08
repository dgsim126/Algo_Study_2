from collections import Counter

T = int(input())
for test_case in range(1, T + 1):
    check_list = list(input())
    word = input()
    word_sort = Counter(word).most_common()

    for i in range(len(word_sort)):
        if word_sort[i][0] in check_list:
            print(f'#{test_case} {word_sort[i][1]}')
            break
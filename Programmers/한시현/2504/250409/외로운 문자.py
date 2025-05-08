T = int(input())
for test_case in range(1, T + 1):
    words = input()
    check_list = list(set(words))

    answer = []
    for word in check_list:
        if words.count(word) % 2 != 0:
            answer.append(word)
    answer.sort()
    str_answer = ''.join(answer)

    if answer:
        print(f'#{test_case} {str_answer}')
    else:
        print(f'#{test_case} Good')


# Counter, dictionary 연습
from collections import Counter

T = int(input())
for test_case in range(1, T + 1):
    words = input()
    word_counter = Counter(words)

    answer = []
    for k, v in word_counter.items():
        if v % 2 != 0:
            answer.append(k)
    answer.sort()

    str_answer = ''.join(answer)
    if answer:
        print(f'#{test_case} {str_answer}')
    else:
        print(f'#{test_case} Good')
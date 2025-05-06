from collections import Counter

T = int(input())
for test_case in range(1, T + 1):
    trash = input()
    words = list(map(str, input().split()))
    words_count = Counter(words)
    answer0 = ['ZRO'] * words_count['ZRO']
    answer1 = ['ONE'] * words_count['ONE']
    answer2 = ['TWO'] * words_count['TWO']
    answer3 = ['THR'] * words_count['THR']
    answer4 = ['FOR'] * words_count['FOR']
    answer5 = ['FIV'] * words_count['FIV']
    answer6 = ['SIX'] * words_count['SIX']
    answer7 = ['SVN'] * words_count['SVN']
    answer8 = ['EGT'] * words_count['EGT']
    answer9 = ['NIN'] * words_count['NIN']

    print(f'#{test_case}', *answer0,*answer1,*answer2,*answer3,*answer4,*answer5,*answer6,*answer7,*answer8,*answer9)
T = int(input())
for test_case in range(1, T + 1):
    trash, n = map(str, input().split())
    nums = list(map(str, input().split()))

    answer0 = ' '.join(['ZRO'] * nums.count('ZRO'))
    answer1 = ' '.join(['ONE'] * nums.count('ONE'))
    answer2 = ' '.join(['TWO'] * nums.count('TWO'))
    answer3 = ' '.join(['THR'] * nums.count('THR'))
    answer4 = ' '.join(['FOR'] * nums.count('FOR'))
    answer5 = ' '.join(['FIV'] * nums.count('FIV'))
    answer6 = ' '.join(['SIX'] * nums.count('SIX'))
    answer7 = ' '.join(['SVN'] * nums.count('SVN'))
    answer8 = ' '.join(['EGT'] * nums.count('EGT'))
    answer9 = ' '.join(['NIN'] * nums.count('NIN'))

    print(f'#{test_case} {answer0} {answer1} {answer2} {answer3} {answer4} {answer5} {answer6} {answer7} {answer8} {answer9}')
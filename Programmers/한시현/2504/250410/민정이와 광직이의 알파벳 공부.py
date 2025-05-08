# 알파벳 총 갯수 : 26
from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())

    count = 0
    for i in range(1, n+1):
        for comb in combinations(words, i):
            s = ''.join(comb)
            s_set = set(s)
            if len(s_set) == 26:
                count += 1

    print(f'#{test_case} {count}')

# 댓글 참고 후 코드 수정
# 입력 조건 중 소문자로만 이루어져 있다는 조건은 잘못되었습니다.
# 중복 제거한 문자열의 길이가 26 인지를 판별하는 방식으로 문제를 풀면 오답이 나옵니다.
# a 부터 z까지 모두 포함되어있는지 체크하는 것을 추천합니다.
from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())

    answer = 0
    for i in range(1, n+1):
        for comb in combinations(words, i):
            count = 0
            s = ''.join(comb)
            s_set = set(s)
            for ss in s_set:
                if ss in 'abcdefghijklmnopqrstuvwxyz':
                    count += 1
            if count == 26:
                answer += 1

    print(f'#{test_case} {answer}')
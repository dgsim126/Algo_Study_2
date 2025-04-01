T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split()) # n:문자열 개수, m:문자열 길이
    words = []
    for _ in range(n):
        words.append(input())

    # 어차피 팰린드롬 성립하려면 뭘 먼저 붙이는가는 상관 없다.
    # 문자열 붙이고 팰린드롬 체크
from collections import deque

T = int(input())
def is_palindrome(s):
    d_s = deque(s)
    while len(d_s) >= 2:
        if d_s.pop() != d_s.popleft():
            return False
    return True

for test_case in range(1, T + 1):
    s = input()
    len_s = len(s)

    mid = len_s // 2
    if len_s % 2 == 0:
        first_s = s[:mid]
        second_s = s[mid:]
    else:
        first_s = s[:mid]
        second_s = s[mid+1:]

    if is_palindrome(s) and is_palindrome(first_s) and is_palindrome(second_s):
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')
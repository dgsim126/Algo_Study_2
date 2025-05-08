# 1 가위 2 바위 3 보
def game(student):
    if len(student) == 1:
        return student[0]
    if len(student) == 2:
        return rsp(student[0], student[1])

    len_s = len(student)
    left = game(student[0:len_s//2])
    right = game(student[len_s//2:])

    return rsp(left, right)

# def rsp(s1, s2):
#     if cards[s1] == 1 and cards[s2] == 2:
#         return s2
#     elif cards[s1] == 2 and cards[s2] == 1:
#         return s1
#     elif cards[s1] == 1 and cards[s2] == 3:
#         return s1
#     elif cards[s1] == 3 and cards[s2] == 1:
#         return s2
#     elif cards[s1] == 2 and cards[s2] == 3:
#         return s2
#     elif cards[s1] == 3 and cards[s2] == 2:
#         return s1
#     else:
#         return s1
# 6/10

# 로직 변경
def rsp(s1, s2):
    if cards[s1] == cards[s2]: # 카드 같으면 번호 작은 사람 승
        return min(s1, s2)
    elif (cards[s1] == 1 and cards[s2] == 3) or (cards[s1] == 2 and cards[s2] == 1) or (cards[s1] == 3 and cards[s2] == 2):
        return s1
    else:
        return s2
# 6/10 뭐임?

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    cards = [0]
    cards.extend(list(map(int, input().split())))
    students = [i for i in range(1, n + 1)]

    print(f'#{test_case} {game(students)}')
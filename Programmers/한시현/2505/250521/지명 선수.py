from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    member = [n for n in range(1, n + 1)]
    a_draft = deque(map(int, input().split()))
    b_draft = deque(map(int, input().split()))

    teamA = []
    teamB = []
    answer = []
    a_turn = True
    while member:
        if a_turn:
            while a_draft:
                a_turn = False
                choose = a_draft.popleft()
                if choose in member:
                    teamA.append(choose)
                    member.remove(choose)
                    break

        elif not a_turn:
            while b_draft:
                a_turn = True
                choose = b_draft.popleft()
                if choose in member:
                    teamB.append(choose)
                    member.remove(choose)
                    break

    for j in range(1, len(teamA)+len(teamB)+1):
        if j in teamA:
            answer.append('A')
        else:
            answer.append('B')

    print(f'{"".join(answer)}')
    #print(f'#{test_case} {"".join(answer)}') # 아.. 출력 형식..
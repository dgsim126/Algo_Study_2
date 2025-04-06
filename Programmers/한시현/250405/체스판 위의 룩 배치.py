# 42/65
T = int(input())
for test_case in range(1, T + 1):
    cant = []
    can = True
    rooks = 0

    for _ in range(8):
        line = input()

        if line.count('O') > 1:
            can = False
            break

        if 'O' in line:
            rooks += 1
            if line.index('O') in cant:
                can = False
                break
            else:
                cant.append(line.index('O'))

    if not can or rooks != 8:
        print(f'#{test_case} no')
    else:
        print(f'#{test_case} yes')

# 40/65 (리팩토링한건데 왜 정답 수 바뀜?)
T = int(input())
for test_case in range(1, T + 1):
    cant = []
    can = True
    rooks = 0

    for _ in range(8):
        line = input()
        if line.count('O') != 1:
            can = False
            break
        else:
            rooks += 1
            if line.index('O') in cant:
                can = False
                break
            else:
                cant.append(line.index('O'))

    if can:
        print(f'#{test_case} yes')
    else:
        print(f'#{test_case} no')
# 진짜 왜 틀렸는지 모르겠음

T = int(input())
for test_case in range(1, T + 1):
    cant = []
    can = True
    rooks = 0

    for _ in range(8):
        line = input()
        if line.count('O') != 1:
            can = False
        else:
            rooks += 1
            if line.index('O') in cant:
                can = False
            else:
                cant.append(line.index('O'))

    if can:
        print(f'#{test_case} yes')
    else:
        print(f'#{test_case} no')
# ㅅㅂ..
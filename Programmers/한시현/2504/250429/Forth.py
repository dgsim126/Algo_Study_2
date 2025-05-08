T = int(input())
for test_case in range(1, T + 1):
    pattern = list(input().split())
    save = []

    for p in pattern:
        if p in ['+', '-', '*', '/']:
            if len(save) >= 2:
                right = save.pop()
                left = save.pop()
                if p == '+':
                    save.append(left + right)
                elif p == '-':
                    save.append(left - right)
                elif p == '*':
                    save.append(left * right)
                else:
                    save.append(left // right)
            else:
                print(f'#{test_case} error')
                break
        else:
            if p == '.':
                if len(save) >= 2:
                    print(f'#{test_case} error')
                    break
                print(f'#{test_case} {save.pop()}')
                break

            save.append(int(p))
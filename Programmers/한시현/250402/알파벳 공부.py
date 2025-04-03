T = int(input())
for test_case in range(1, T + 1):
    alpha = input()
    count = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(alpha)):
        if alpha[i] == alphabet[i]:
            count += 1
        else:
            break

    print(f'#{test_case} {count}')
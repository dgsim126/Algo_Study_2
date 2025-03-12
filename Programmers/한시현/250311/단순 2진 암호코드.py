T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    square = []

    case9 = '0001011'
    case8 = '0110111'
    case7 = '0111011'
    case6 = '0101111'
    case5 = '0110001'
    case4 = '0100011'
    case3 = '0111101'
    case2 = '0010011'
    case1 = '0011001'
    check = '0'*56

    for _ in range(N):
        square.append(input())

    codes = []
    numbers = []
    for row in range(N-8+1):
        for col in range(M-56+1):
            if square[row][col:col+56] != check:
                code = square[row:row+56][col]
                codes.append(code[:7])
                codes.append(code[7:14])
                codes.append(code[14:21])
                codes.append(code[21:28])
                codes.append(code[28:35])
                codes.append(code[35:42])
                codes.append(code[42:49])
                codes.append(code[49:])

                for code in codes:
                    if code == case1:
                        numbers.append(1)
                    elif code == case2:
                        numbers.append(2)
                    elif code == case3:
                        numbers.append(3)
                    elif code == case4:
                        numbers.append(4)
                    elif code == case5:
                        numbers.append(5)
                    elif code == case6:
                        numbers.append(6)
                    elif code == case7:
                        numbers.append(7)
                    elif code == case8:
                        numbers.append(8)
                    else:
                        numbers.append(9)
        break

    if len(numbers) == 8:
        check_code = (numbers[0]+numbers[2]+numbers[4]+numbers[6])*3 + numbers[1]+numbers[3]+numbers[5]+numbers[7]

        if str(check_code)[-1] == '0':
            print(f'#{test_case} {sum(numbers)}')
        else:
            print(f'#{test_case} ', 0)
    else:
        print(f'#{test_case} ', 0)
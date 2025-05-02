for test_case in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    while dump > 0:
        highest = box.index(max(box))
        lowest = box.index(min(box))
        box[highest] -= 1
        box[lowest] += 1
        dump -= 1

    print(f'#{test_case} {max(box) - min(box)}')
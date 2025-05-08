for test_case in range(10):
    dump = int(input())
    box_height = list(map(int, input().split()))

    for _ in range(dump):
        max_height = max(box_height)
        max_index = box_height.index(max_height)
        box_height[max_index] -= 1

        min_height = min(box_height)
        min_index = box_height.index(min_height)
        box_height[min_index] += 1

    print(f'#{test_case + 1} {max(box_height) - min(box_height)}')
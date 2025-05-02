from collections import deque

def bfs(start):
    q = deque([start])
    count = 0

    while q:
        node = q.popleft()
        count += 1
        for child in tree[node]:
            q.append(child)

    return count

T = int(input())
for test_case in range(1, T + 1):
    e, n = map(int, input().split())
    nums = list(map(int, input().split()))

    tree = [[] for _ in range(e + 2)]

    for i in range(0, len(nums), 2):
        parent = nums[i]
        child = nums[i+1]
        tree[parent].append(child)

    result = bfs(n)
    print(f'#{test_case} {result}')
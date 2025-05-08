def solution(N, wires):
    answer = 0
    wires = sorted(wires, key=lambda x: x[0])
    for i in range(len(wires)-1):
        ay = wires[i][1]
        for j in range(i+1, len(wires)):
            by = wires[j][1]
            if by < ay:
                answer += 1
    
    return answer

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    wires = []
    for _ in range(N):
        wires.append(list(map(int, input().split())))

    answer = solution(N, wires)
    print(f"#{test_case} {answer}")
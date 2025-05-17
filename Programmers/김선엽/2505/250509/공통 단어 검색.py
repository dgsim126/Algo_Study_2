def solution(note_a, note_b):
    answer = 0
    note_a = set(note_a)
    for i in range(len(note_b)):
        if note_b[i] in note_a:
            answer += 1

    return answer

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    note_a = []
    note_b = []
    for _ in range(N):
        note_a.append(input())
    for _ in range(M):
        note_b.append(input())
    answer = solution(note_a, note_b)
    print(f"#{test_case} {answer}")
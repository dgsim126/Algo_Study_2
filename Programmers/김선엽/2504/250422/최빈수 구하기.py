def solution(scores):
    var = [0] * 101
    print(var[100])
    for score in scores:
        var[100-score] += 1
    
    return 100-var.index(max(var))
    
T = int(input())
for _ in range(T):
    n = int(input())
    scores = []
    while len(scores) < 1000:
        scores.extend(map(int, input().split()))

    answer = solution(scores)
    print(f"#{n} {answer}")
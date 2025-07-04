def solution(N, trees):
    # 가장 큰 나무 높이를 찾음 (모든 나무를 이 높이까지 자라게 해야 함)
    max_height = max(trees)

    even = 0  # 2단씩 자라는 날에 필요한 횟수 누적
    odd = 0   # 1단씩 자라는 날에 필요한 횟수 누적

    for t in trees:
        diff = max_height - t  # 각 나무가 자라야 할 높이 차이

        even += diff // 2      # 2단씩 자라게 하는 날에 필요한 횟수 누적
        odd += diff % 2        # 나머지 1단씩 자라야 하는 날은 odd에 누적

    # 그리디하게 자라게 하되, 번갈아가며 1과 2를 쓰는 방식으로 최적화가 필요
    # 2단 자람이 1단 자람보다 많을 때는, 2를 줄이고 1을 늘려서 균형을 맞춤
    # 이는 "2, 2"를 "1, 1, 1"로 바꿔서 더 나은 방식으로 일 수를 줄이기 위함
    if even > odd:
        while abs(even - odd) > 1:
            even -= 1
            odd += 2  # 2단 자람 1회를 없애고 1단 자람 2회로 대체 (실질적으로 더 효율적인 구조)

    # 최종적으로 결과 계산
    if odd > even:
        # 1단 자람이 많다면, "1, 2, 1, 2..." 형태로 진행되기 때문에
        # 1단 자람 수 * 2 - 1 (마지막에 1만 쓰고 끝낼 수 있음)
        result = odd * 2 - 1
    elif even > odd:
        # 2단 자람이 많다면, 그냥 2, 2, 2... 형태로 가능하므로 2 * even
        result = even * 2
    else:
        # 1단과 2단 자람 수가 같다면, 1, 2, 1, 2,... 완전히 번갈아 가능
        result = even + odd

    return result


# 테스트 실행
N = 20
trees = [4, 5, 3, 4, 2, 4, 4, 3, 5, 2, 2, 3, 5, 5, 5, 2, 5, 2, 5, 5]
print(solution(N, trees))  # => 최소한의 일 수 출력

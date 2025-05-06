T = int(input())  # 테스트 케이스 개수 입력

for tc in range(1, T+1):
    N = int(input())  # 수열의 길이 입력
    arr = list(map(int, input().split()))  # 수열 입력
    dp = [1] * N  # LIS 길이를 저장하는 dp 배열, 최소값 1

    print(f"\n### Test Case {tc}: N={N}, arr={arr}\n")
    print(f"초기 dp 배열: {dp}\n")

    for i in range(N):  # i번째 원소 기준으로
        for j in range(i + 1, N):  # i 이후의 원소 j 탐색
            print(f"i={i}({arr[i]}), j={j}({arr[j]}) -> ", end="")
            if arr[i] <= arr[j]:  # 증가하는 경우 (같거나 커야 함)
                dp[j] = max(dp[i] + 1, dp[j])  # 최장 증가 부분 수열 길이 갱신
                print(f"조건 만족! dp[{j}] = max(dp[{i}] + 1, dp[{j}]) → {dp[j]}")
            else:
                print("조건 불만족 (변화 없음)")

        print(f"dp 상태 (i={i} 기준): {dp}\n")  # i 루프 한 번 끝날 때 dp 출력

    print(f"최종 dp 배열: {dp}")
    print(f"#{tc} {max(dp)}")  # 최장 증가 부분 수열 길이 출력

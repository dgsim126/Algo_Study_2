T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f"#{test_case} {max(numbers) - min(numbers)}")
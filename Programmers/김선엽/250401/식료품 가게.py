def solution(sales):
    answer = []
    sales_ = sales[:]
    for i in range(len(sales)):
        price = sales[i] * (4/3)
        if price in sales_ and sales[i] in sales_:
            sales_.pop(sales_.index(price))
            sales_.pop(sales_.index(sales[i]))
            answer.append(sales[i])
    return answer

# print(solution([15, 20, 60, 75, 80, 100]))
# print(solution([90, 90, 120, 120, 120, 150, 160, 200]))

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    sales = list(map(int, input().split()))
    answer = solution(sales)
    print(f"#{test_case}", *answer)
from collections import deque

def solution(N, secrets, order_N, orders):
    orders= deque(orders)
    for i in range(order_N):
        orders.popleft()
        point= int(orders.popleft())
        len_= int(orders.popleft())
        temp= []
        for i in range(len_):
            temp.append(orders.popleft())

        secrets= secrets[0:point]+temp+secrets[point:]
        # print(secrets)

    return secrets[0:10]


## main ##
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N= int(input())
    secrets= list(input().split())
    order_N= int(input())
    orders= list(input().split())
    print(f"#{test_case}", *solution(N, secrets, order_N, orders)) # 출력 양식 실패 1회
# N= 11
# secrets= [449047, 855428, 425117, 532416, 358612, 929816, 313459, 311433, 472478, 589139, 568205]
# order_N= 7
# orders= ['I', '1', '5', '400905', '139831', '966064', '336948', '119288', 'I', '8', '6', '436704', '702451', '762737', '557561', '810021', '771706', 'I', '3', '8', '389953', '706628', '552108', '238749', '661021', '498160', '493414', '377808', 'I', '13', '4', '237017', '301569', '243869', '252994', 'I', '3', '4', '408347', '618608', '822798', '370982', 'I', '8', '2', '424216', '356268', 'I', '4', '10', '512816', '992679', '693002', '835918', '768525', '949227', '628969', '521945', '839380', '479976']
# print(solution(N, secrets, order_N, orders))
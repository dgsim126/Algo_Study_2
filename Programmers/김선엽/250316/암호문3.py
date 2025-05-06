def solution(n, bundle, m, orders):
    i = 0
    while m > 0:
        if orders[i] == "A":
            length = int(orders[i+1])
            add_list = orders[i+2:i+2+length]
            bundle.extend(add_list)
            i += (length + 2)
            m -= 1
        elif orders[i] == "I":
            index = orders[i+1]
            length = orders[i+2]
            add_list = orders[i+3:i+3+length]
            list_a = bundle[:index]     ## index 주의
            list_b = bundle[index:]
            list_a.extend(add_list)
            bundle = list_a.extend(list_b)
            i += (length + 3)
            m -= 1
        elif orders[i] == "D":
            index = orders[i+1]
            length = orders[i+2]
            list_a = bundle[:index]
            list_b = bundle[index+length:]
            bundle = list_a.extend(list_b)
            i += 3
            m -= 1
        
        print(bundle)

    return bundle[:10]

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    bundle = list(map(str, input().split()))
    m = int(input())
    orders = list(map(str, input().split()))

    answer = solution(n, bundle, m, orders)
    print(f"#{test_case}", *answer)

# 31
# 801199 482510 422184 242474 876697 940126 116534 339876 247263 458098 825098 223019 514111 303365 893555 243643 601338 454353 574796 689563 658854 865075 999888 791926 506889 150144 881247 837754 384870 933366 151318
# 2
# A 3 1 2 3 D 2 2

# num_list = list(map(str, input().split()))
# print(len(num_list))

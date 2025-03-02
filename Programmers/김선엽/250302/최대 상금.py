def solution(num, trial):
    num_list = list(str(num))
    i = 0
    while trial > 0:
        print(num_list)
        if i == len(num_list):
            if trial % 2 == 0:
                break
            else:
                num_list[-1], num_list[-2] = num_list[-2], num_list[-1]


        cur = int(num_list[i])
        max = 0
        max_i = 0

        for index in range(i+1, len(num_list)):
            if int(num_list[index]) >= max:
                max = int(num_list[index])
                max_i = index
        
        if max > cur:
            num_list[i], num_list[max_i] = num_list[max_i], num_list[i]
            i += 1
            trial -= 1
        else:
            i += 1
        
    return int("".join(num_list))

print(solution(123, 1))
print(solution(32888, 2))
print(solution(2737, 1))
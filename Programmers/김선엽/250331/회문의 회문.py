def solution(string):
    length = len(string)
    half = int((length - 1) / 2)
    if string == string[::-1]:
        part1 = string[:half]
        part2 = string[half+1:]
        # print(part1, part2) 이 부분 포함해서 틀림..
        if part1 == part1[::-1] and part2 == part2[::-1]:
            return 1    
    return 0

T = int(input())
for test_case in range(1, T+1):
    string = input()

    if solution(string):
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")
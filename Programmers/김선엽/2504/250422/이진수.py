def solution(n, number):
    dic_x = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    result = ""

    for i in range(int(n)):
        result += dic_x[number[i]]
    
    return result

T = int(input())
for test_case in range(1, T+1):
    n, number = map(str, input().split())
    answer = solution(n, number)
    print(f"#{test_case} {answer}")
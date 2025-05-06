def solution(string):
    word = []
    zz = ("a", "e", "i", "o", "u")
    for i in range(len(string)):
        if string[i] not in zz:
            word.append(string[i])
    
    return "".join(word)

T = int(input())
for test_case in range(1, T+1):
    string = input()
    answer = solution(string)

    print(f"#{test_case} {answer}")
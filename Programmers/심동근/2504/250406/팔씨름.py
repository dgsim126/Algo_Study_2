def solution(games):
    current_times= len(games)
    i_win= 0

    for i in range(len(games)):
        if(games[i]=="o"):
            i_win+=1

    if(current_times==15):
        if(i_win>=8):
            return "YES"
        return "NO"

    if((8-i_win)/(15-current_times)<=1):
        return "YES"
    return "NO"

## main ##
T = int(input())
for test_case in range(1, T + 1):
    games= input()
    print(f"#{test_case} {solution(games)}")
# games= "oxoxoxoxoxoxoxo"
# print(solution(games))
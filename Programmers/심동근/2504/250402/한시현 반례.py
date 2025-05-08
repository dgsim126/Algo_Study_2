def solution(S, T):
    while len(S) < 100:
        S += S
    while len(T) < 100:
        T += T

    if S[:100] == T[:100]:
        return "yes"
    else:
        return "no"

## main ##
S= "abababababab"
T= "abab"
print(solution(S, T))
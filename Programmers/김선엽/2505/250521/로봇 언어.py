def solution(lang):
    loc = 0
    loc_set = set()
    count = 0
    print(lang)
    for i in range(len(lang)):
        if lang[i] == "L":
            loc -= 1
            loc_set.add(abs(loc))
        elif lang[i] == "R":
            loc += 1
            loc_set.add(abs(loc))
        else:
            count += 1
    if loc_set:
        if max(loc_set) >= min(loc_set):
            return max(loc_set) + count
        else:
            return min(loc_set) + count
    else:
        return count

T = int(input())
for test_case in range(1, T+1):
    lang = input()
    answer = solution(list(lang))
    print(answer)

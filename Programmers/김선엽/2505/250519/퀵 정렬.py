def quick_sort(list_):
    if len(list_) > 2:
        pivot = list_[0]
        A = []
        B = []
        for i in range(1, len(list_)):
            if list_[i] < pivot:
                A.append(list_[i])
            else:
                B.append(list_[i])
        if A and B:
            return quick_sort(A) + [pivot] + quick_sort(B)
        if A and not B:
            return quick_sort(A) + [pivot]
        else:
            return [pivot] + quick_sort(B)

    elif len(list_) == 2:
        if list_[1] >= list_[0]:
            return list_
        else:
            return list_[::-1]
    elif len(list_) == 1:
        return list_
    else:
        return []

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = quick_sort(numbers)
    print(f"#{test_case} {answer[N//2]}")
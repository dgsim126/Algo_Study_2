## 풀이

def solution(nums):
    def findXY(num):
        i = 1
        first = 1
        while True:
            if num < first:
                break
            else:
                first += i
                i += 1
        first -= (i - 1)
        start = [1, i - 1]
        for i in range(first, num):
            start[0] += 1
            start[1] -= 1

        return start
    
    def findNum(XY):
        i = 0
        x, y = XY
        
        if x > 1:
            minus = x - 1
            x -= minus
            i += minus
            y += minus
        
        num = 1
        cur = 1
        while True:
            if y == num:
                return cur + i
            else:
                cur += num
                num += 1

    x1, y1 = findXY(nums[0])
    x2, y2 = findXY(nums[1])

    nx, ny = x1 + x2, y1 + y2

    return findNum([nx, ny])


print(solution([3,9]))


## 제출

T = int(input())
def solution(nums):
    def findXY(num):
        i = 1
        first = 1
        while True:
            if num < first:
                break
            else:
                first += i
                i += 1
        first -= (i - 1)
        start = [1, i - 1]
        for i in range(first, num):
            start[0] += 1
            start[1] -= 1
 
        return start
     
    def findNum(XY):
        i = 0
        x, y = XY
         
        if x > 1:
            minus = x - 1
            x -= minus
            i += minus
            y += minus
         
        num = 1
        cur = 1
        while True:
            if y == num:
                return cur + i
            else:
                cur += num
                num += 1
 
    x1, y1 = findXY(nums[0])
    x2, y2 = findXY(nums[1])
 
    nx, ny = x1 + x2, y1 + y2
 
    return findNum([nx, ny])
 
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    answer = solution(nums)
     
    print(f"#{test_case} {answer}")
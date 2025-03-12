# 풀이, 시간제한 30초, 문장 길이 제한
from collections import deque

def solution(find, string):
    length = len(find)
    queue = deque([])
    find = deque(list(find))
    count = 0
    for i in range(len(string)):
        if not queue or len(queue) < length:
            queue.append(string[i])
        else:
            queue.popleft()
            queue.append(string[i])

        if queue == find:
            count += 1
        
    return count

# print(solution("ti", "Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition."))
# print(solution("ing", "Thedoublehelixformsthestructuralbasisofsemi-conservativeDNAreplication.1,2Lessintuitively,italsohasimplicationsontheinformationcontentofDNAfordouble-strandedDNAassuchonlyhasabouthalfthestoragecapacityofsingle-strandedDNA.Thisisbecauseagivensequenceanditsreversecomplement,whilethesameinthedouble-strandedform,aredifferententitiesinsingle-strandedDNA?exceptforthosesequenceswhichareidenticaltotheirreversecomplement"))

# 풀이

for test_case in range(1, 11):
    T = int(input())
    find = input()
    string = input()
    length = len(find)
    count = 0
    for i in range(len(string)-length + 1):
        if string[i:i+length] == find:
            count += 1
 
    print(f"#{T} {count}")
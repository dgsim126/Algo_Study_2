import heapq

list= [9,8,7,6,5,4]

heapq.heapify(list)
print(list)

val= 3

heapq.heappush(list, -val)
print(list)

print(heapq.heappop(list), "fuck")
print(list)

list.append(100)
print(list)


print(type(list))
from collections import deque

clothes = list(map(int, input().split()))  
shelf_capacity = int(input())  
shelves_used = 0  
current_shelf_load = 0  
stack = deque()  

for item in clothes:
    while current_shelf_load + item > shelf_capacity:
        current_shelf_load -= stack.pop()
    stack.append(item)
    current_shelf_load += item

shelves_used = len(stack)

print(shelves_used)

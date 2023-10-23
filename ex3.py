from collections import deque
food_quantity = int(input())  
orders = deque(map(int, input().split()))  

max_order = max(orders)
print(max_order)

while orders:
    current_order = orders.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        orders.appendleft(current_order)  
        break

if not orders:
    print("Orders complete")
else:
    remaining_orders = ", ".join(map(str, orders))
    print(f"Orders left: {remaining_orders}")
from collections import deque

def solution(priorities, location):
    orders = deque([i for i in range(len(priorities))])
    priorities = deque(priorities)
    pop_count = 0
    while len(priorities) > 0:
        curr_max = max(priorities)
        prior = priorities.popleft()
        order = orders.popleft()
        if prior != curr_max:
            priorities.append(prior)
            orders.append(order)            
            continue
        pop_count += 1
        if order == location:
            return pop_count

print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5
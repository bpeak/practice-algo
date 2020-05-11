# me
def solution(departmentApplyBudgetList, totalBudget):
    supportedDepartmentCount = 0
    leftBudget = totalBudget
    
    while True:
        if len(departmentApplyBudgetList) == 0:
            break
        
        minApplyBudget = min(departmentApplyBudgetList)
        minApplyBudgetIdx = departmentApplyBudgetList.index(minApplyBudget)
        
        if minApplyBudget > leftBudget:
            break
        
        departmentApplyBudgetList.pop(minApplyBudgetIdx)
        leftBudget -= minApplyBudget
        supportedDepartmentCount += 1
        
    return supportedDepartmentCount

print(solution([1,3,2,5,4], 9)) # 3
print(solution([2,2,3,3], 10)) # 4

"""
최대 최소 와 관련된 문제에서
"정렬"은 굉장히 유용한 아이디어 일 수 있음
나는 현재 정렬되지 않은 리스트라서
매번 min을 새로 구하는데
차라리 한번 솔팅해놓는게 좋은 선택일 수 있음


"""
# best ( 근데 why? )
def solution2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

print(solution2([1,3,2,5,4], 9)) # 3
print(solution2([2,2,3,3], 10)) # 4
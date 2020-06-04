def solution(skill_order, skill_trees):
    skill_order_set = set(skill_order)
    result = 0 # 가능한 스킬트리 갯수
    for skill_tree in skill_trees:
        next_skill_idx = 0
        is_possible_skill_tree = True
        for skill in skill_tree:
            if skill not in skill_order_set:
                continue
            curr_skill_idx = skill_order.index(skill)
            if skill != skill_order[next_skill_idx]:
                is_possible_skill_tree = False
                break
            next_skill_idx += 1
        if is_possible_skill_tree:
            result += 1
    return result
            
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

"""
1. for else 를 사용할 수 있다는것
2. 항상 조기 continue 나 조기 break 가 좋은걸까?
    지금보면 밑의 로직이 훨씬 이해하기가 쉬운것같아. ( 현재 상황에서는 밑의 케이스가 더 이해도가 높아보임 )
4. list 복사할때 copy 쓰면 되는데
    그냥 list(target_list) 도 복사됨
    근데 string 은 copy 사용할 수 없으니 ( 엄밀히 list가 아니잖아 )
    list(string) 이 좋겠군
3. 사실 pop 0은 좋지 않음 ( collection 써야함 ( O(1)같아 보이지만 O(n)임 ) )
"""
def solution2(skill_order, skill_trees):
    skill_order_set = set(skill_order)
    result = 0
    for skill_tree in skill_trees:
        skill_order_local = list(skill_order)
        for skill in skill_tree:
            if skill in skill_order_set and skill != skill_order_local.pop(0):
                break
        else:
            result += 1
    return result


print(solution2("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))

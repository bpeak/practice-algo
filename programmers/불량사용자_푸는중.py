# https://programmers.co.kr/learn/courses/30/lessons/64064
# 코드정리...

candidate = []

def find(ids_list, idx=0, result=[]):
    if len(ids_list) == idx:
        candidate.append(result)
        return
    for _id in ids_list[idx]:
        copied_result = result.copy()
        copied_result.append(_id)
        find(ids_list, idx + 1, copied_result)


def solution(user_ids, banned_ids):
    possible_ids_list = []
    for banned_id in banned_ids:
        possible_ids = []
        for user_id in user_ids:
            if len(banned_id) != len(user_id):
                continue
            for i, banned_id_char in enumerate(banned_id):
                user_id_char = user_id[i]
                if banned_id_char != "*" and user_id_char != banned_id_char: break
            else:
                possible_ids.append(user_id)
        possible_ids_list.append(possible_ids)

    find(possible_ids_list)
    used = set()
    count = 0
    for ids in candidate:
        if len(set(ids)) != len(ids): continue
        s = "".join(sorted(ids))
        if s not in used:
            used.add(s)
            count += 1
    return count

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) # 2
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) # 3
	
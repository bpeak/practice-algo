def solution(records):
    logs = []
    nicknames = {}
    for record in records:
        tokens = record.split(" ")
        action = tokens[0]
        uid = tokens[1]

        # Leave
        if action == 'Leave':
            logs.append({
                "uid": uid,
                "action": action,
            })
            continue

        # Enter or Change 일 경우 닉네임 적용
        nickname = tokens[2]
        nicknames[uid] = nickname

        if action == 'Enter':
            logs.append({
                "uid": uid,
                "action": action,
            })

    results = []
    for log in logs:
        msg = ""
        msg += nicknames[log.get("uid")]
        if log.get('action') == 'Enter':
            msg += "님이 들어왔습니다."
        elif log.get('action') == 'Leave':
            msg += "님이 나갔습니다."
        results.append(msg)
    return results

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

"""
typedef User {
    uid,
    action,
}

nicknames = {
    "uid1234": "고길동"
}

레코드 반복
    Enter
        logs에 user(입장) 추가
        nicknames[id] = nickname
    Leavn
        logs에 user(퇴장) 추가
    Change
        nicknames[id] = nickname

로그 반복
    nicnames로 logs생성

"""

def solution2(records):
    logs = []
    nicnames = {}
    for record in records:
        tokens = record.split(" ")
        logs.append({
            "uid": tokens[1],
            "action": tokens[0]
        })
        if tokens[0] in ['Enter', 'Change']:
            nicnames[tokens[1]] = tokens[2]
    
    msgs = {'Enter': "님이 들어왔습니다.", 'Leave': "님이 나갔습니다."}
    results = []
    for log in logs:
        if log.get('action') != 'Change':
            results.append(nicnames[log.get('uid')] + msgs[log.get('action')])
    return results

print(solution2(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
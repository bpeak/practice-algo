def solution(p):
    if p == "": 
        return ""
    start_bracket = p[0]
    stack = [start_bracket]
    count = 1
    idx = 1
    sub_bracket_start_idx = 0
    while True:
        curr_bracket = p[idx]
        stack.append(curr_bracket)
        if start_bracket == curr_bracket: 
            count += 1
        else:
            count -= 1
        idx += 1
        if count == 0:
            sub_bracket_start_idx = idx
            break
    
    u = p[:idx]
    v = p[idx:]
    
    print(u, v)

print(solution("()))((()"))
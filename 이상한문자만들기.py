def solution(str):
    result = ""
    idx = 0
    for c in str:
        if c == " ":
            idx = 0
        else:
            if idx % 2 == 0:
                c = c.upper()
            else:
                c = c.lower()
            idx += 1
        result += c
    return result
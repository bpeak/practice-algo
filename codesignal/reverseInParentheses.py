import time
from collections import deque

#
def solution_(s):
    b1 = []
    b2 = deque()
    for i, c in enumerate(s):
        if c == "(":
            b1.append(i)
        elif c == ")":
            b2.append(i)
    for i in range(len(b1)):
        i1 = b1.pop()
        # [try 1] pop()
        # [try 2] popleft()
        i2 = b2.popleft()
        s = s[:i1] + s[i1:i2+1][::-1] + s[i2+1:]
    return "".join([c for c in s if c not in ('(', ')')])

def solution(s):
    b1 = []
    b2 = deque()
    for i, c in enumerate(s):
        if c == "(":
            b1.append(i)
        elif c == ")":
            b2.append(i)
        if len(b1) == len(b2):
            for i in range(len(b1)):
                i1 = b1.pop()
                i2 = b2.popleft()
                s = s[:i1] + s[i1:i2+1][::-1] + s[i2+1:]
    return "".join([c for c in s if c not in ('(', ')')])    

print(solution("foo(bar(baz))blim"))
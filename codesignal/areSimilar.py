def areSimilar(a, b):
    if a == b: return True
    anum = []
    bnum = []
    for i in range(len(a)):
        if a[i] != b[i]:
            anum.append(a[i])
            bnum.append(b[i])
        if len(anum) > 2:
            return False
    else:
        if len(anum) == 1:
            return False
        if anum[0] == bnum[1] and anum[1] == bnum[0]:
            return True
        return False

print(areSimilar([1, 2, 3], [2, 1, 3])) # 1
print(areSimilar([1, 2, 2],[2, 1, 1])) # 0

def areSimilar2(a, b):
    return sorted(a) == sorted(b) and sum([ac != bc for ac, bc in zip(a, b)]) == 2

print(areSimilar2([1, 2, 3], [2, 1, 3])) # 1
print(areSimilar2([1, 2, 2],[2, 1, 1])) # 0
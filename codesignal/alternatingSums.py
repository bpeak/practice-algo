def alternatingSums(arr):
    r1 = 0
    r2 = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            r1 += arr[i]
        else:
            r2 += arr[i]
    return [r1, r2]

print(alternatingSums([50, 60, 60, 45, 70])) # [180, 105]

def alternatingSums2(arr):
    return [sum(arr[::2]), sum(arr[1::2])]

print(alternatingSums2([50, 60, 60, 45, 70]))

a = [1,2,3,4,5,6,7,8,9,10]

# a[start:end:step]
print(a)
print(a[4:])
print(a[:4])
print(a[::-1]) # reverse step
print(a[::2])
print(a[::3])
print(a[::4])




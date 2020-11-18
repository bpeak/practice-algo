def addBorder(picture):
    result = ["*" + s + "*" for s in picture]
    count = len(picture[0])
    result.insert(0, "*" * (count + 2))
    result.append("*" * (count + 2))
    return result

print(addBorder(["abc","ded"]))
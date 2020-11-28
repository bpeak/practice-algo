def variableName(name):
    if name[0].isdigit() or not (name[0].isalpha() or name[0] == '_'):
        return False
    for c in name:
        if c.isalpha() or c.isdigit() or c == '_':
            continue
        return False
    return True

'''
isidentifier
def variableName2(name):
    return name.isidentifier()


js
function variableName(name) {
  return /^[a-z_]\w*$/i.test(name)
}
'''

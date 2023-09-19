def constructPath(oldPath, newPath):
    if newPath[0] == '/':
        oldPath = newPath
        if (newPath[-1] != '/'):
            oldPath += "/"
    else:
        dirs = newPath.split('/')
        for dir in dirs:
            if dir == "." or dir == "":
                pass
            elif dir == "..":
                idx = oldPath.rfind("/", 0, -1)
                oldPath = oldPath[:idx] + "/"
            else:
                oldPath += dir + "/"
    return oldPath

def printStatus(status):
    print(f"Error. Status: {status}")
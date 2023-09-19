import sys

def exec(hdfs, cmd):
    cmd = cmd.split()

    if len(cmd) == 0:
        return
    if cmd[0] == "mkdir" and len(cmd) == 2:
        hdfs.mkdir(cmd[1])
    elif cmd[0] == "put" and len(cmd) == 2:
        fileName = cmd[1].split('/')[-1]
        hdfs.put(cmd[1], fileName)
    elif cmd[0] == "get" and len(cmd) == 3:
        hdfs.get(cmd[1], cmd[2])
    elif cmd[0] == "append" and len(cmd) == 3:
        hdfs.append(cmd[1], cmd[2])
    elif cmd[0] == "delete" and len(cmd) == 2:
        hdfs.delete(cmd[1])
    elif cmd[0] == "ls" and len(cmd) == 1:
        hdfs.ls()
    elif cmd[0] == "cd" and len(cmd) == 2:
        hdfs.cd(cmd[1])
    elif cmd[0] == "lls" and len(cmd) == 1:
        hdfs.lls()
    elif cmd[0] == "lcd" and len(cmd) == 2:
        hdfs.lcd(cmd[1])
    elif cmd[0] == "exit":
        sys.exit()
    else:
        print("Incorrect command")

import sys

import client
from main import HOST, PORT, USER


def parse_cmd(cmd):
    hdfs = client.HDFS(HOST, PORT, USER)

    cmd = cmd.split()
    if cmd[0] == "mkdir" and len(cmd) == 2:
        hdfs.mkdir(cmd[1])
    elif cmd[0] == "ls" and len(cmd) == 1:
        hdfs.ls()
    elif cmd[0] == "put" and len(cmd) == 2:
        fileName = cmd[1].split('/')[-1]
        hdfs.put(cmd[1], fileName)
    elif cmd[0] == "delete" and len(cmd) == 2:
        hdfs.delete(cmd[1])
    elif cmd[0] == "lls" and len(cmd) == 1:
        client.lls()
    elif cmd[0] == "lcd" and len(cmd) == 2:
        client.lcd(cmd[1])
    elif cmd[0] == "exit":
        sys.exit()

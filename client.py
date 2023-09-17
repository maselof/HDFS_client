#ОСТАЛОСЬ ЕБАНУТЬ get, cd
#И ВСЕ ПРОВЕРИТЬ
#LCD РАБОТАЕТ ОХУИТЕЛЬНО, САМ В АХУЕ
import os
import requests

HISTORY_PATH_HDFS = "/"
HISTORY_PATH_LOCAL = "/home/"


class HDFS:
    def __init__(self, host, port, user):
        self.host = host
        self.port = port
        self.user = user
        self.home = f"http://{host}:{port}/webhdfs/v1/user/{self.user}"

    def mkdir(self, nameDir):
        response = requests.put(f"{self.home}{HISTORY_PATH_HDFS}{nameDir}",
                                params={"user.name": self.user,
                                        "op": "MKDIRS"})
        if response.status_code == 200:
            print("The directory was successfully created")
        else:
            print("Something went wrong")

    def put(self, localFileName, hdfsFileName):
        data = open(localFileName, "r").read
        response = requests.put(f"{self.home}{HISTORY_PATH_HDFS}{hdfsFileName}",
                                params={"user.name": self.user,
                                        "op": "CREATE",
                                        "overwrite": "true"})
        url = response.url
        response = requests.put(url=url, data=data())
        if response.status_code == 201:
            print("File downloaded")
        else:
            print("Something went wrong")

    def append(self, localFileName, hdfsFileName):
        data = open(HISTORY_PATH_LOCAL + localFileName, "r").read
        response = requests.post(f"{self.home}{HISTORY_PATH_HDFS}{hdfsFileName}",
                                 params={"user.name": self.user,
                                         "op": "APPEND"})
        url = response.url
        response = requests.post(url=url, data=data())
        if response.status_code == 201:
            print("File appended")
        else:
            print("Something went wrong")

    def ls(self):
        response = requests.get(f"{self.home}{HISTORY_PATH_HDFS}",
                                params={"user.name": self.user,
                                        "op": "LISTSTATUS"})
        dirOrFiles = dict(response.json())
        directories = list()
        files = list()
        for file in dirOrFiles["FileStatuses"]["FileStatus"]:
            if file["type"] == "DIRECTORY":
                directories.append(file["pathSuffix"])
            elif file["type"] == "FILE":
                files.append(file["pathSuffix"])
        print("DIRECTORIES")
        for directory in directories:
            print(directory)
        print("FILES")
        for file in files:
            print(file)

    def delete(self, fileName):
        response = requests.delete(f"{self.home}{HISTORY_PATH_HDFS}{fileName}",
                                   params={"user.name": self.user,
                                           "op": "DELETE"})

        if response.status_code == 200:
            print("The deletion was successful")
        else:
            print("Something went wrong")


def lls():
    os.system(f"ls {HISTORY_PATH_LOCAL}")


def lcd(dirName):
    global HISTORY_PATH_LOCAL
    if dirName == '..':
        paths = HISTORY_PATH_LOCAL.split("/")
        HISTORY_PATH_LOCAL = '/'
        for i in range(2):
            del paths[-1]
        for symbol in paths:
            if symbol != '':
                HISTORY_PATH_LOCAL += f"{symbol}/"
    else:
        check = os.system(f"cd {HISTORY_PATH_LOCAL}{dirName}")
        if check == 0:
            HISTORY_PATH_LOCAL += f"{dirName}/"





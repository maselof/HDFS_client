import os

import requests

HISTORY_PATH_HDFS = list(["/"])
HISTORY_PATH_LOCAL = list(["/"])


class HDFS:
    def __init__(self, host, port, user):
        self.host = host
        self.port = port
        self.user = user
        self.home = f"http://{host}:{port}/webhdfs/v1/user/{self.user}"

    def mkdir(self, nameDir):
        response = requests.put(f"{self.home}{HISTORY_PATH_HDFS[-1]}{nameDir}",
                                params={"user.name": self.user,
                                        "op": "MKDIRS"})
        if response.status_code == 200:
            print("The directory was successfully created")
        else:
            print("Something went wrong")

    def put(self, path, fileName):
        data = open(path, "r").read
        response = requests.put(f"{self.home}{HISTORY_PATH_HDFS[-1]}{fileName}",
                                params={"user.name": self.user,
                                        "op": "CREATE",
                                        "overwrite": "true"})
        url = response.url
        response = requests.put(url=url, data=data())
        if response.status_code == 201:
            print("")

    def append(self, path, fileName):
        response = requests.post(f"{self.home}{HISTORY_PATH_HDFS[-1]}{fileName}",
                                 params={"user.name": self.user,
                                         "op": "APPEND"})
        url = response.url

    def ls(self):
        response = requests.get(f"{self.home}{HISTORY_PATH_HDFS[-1]}",
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

    def delete(self, path):
        response = requests.delete(f"{self.home}{HISTORY_PATH_HDFS[-1]}{path}",
                                   params={"user.name": self.user,
                                           "op": "DELETE"})

        if response.status_code == 200:
            print("The deletion was successful")
        else:
            print("Something went wrong")


def lls():
    os.system("ls")


def lcd(path):
    os.system(f"cd {path}")

import os
import requests
import utils

class HDFS:
    def __init__(self, host, port, user):
        self.current_path = "/"
        self.local_current_path = "/home/"
        self.host = host
        self.port = port
        self.user = user
        self.home = f"http://{host}:{port}/webhdfs/v1/user/{self.user}"

    def mkdir(self, nameDir):
        response = requests.put(f"{self.home}{self.current_path}{nameDir}",
                                params={"user.name": self.user,
                                        "op": "MKDIRS"})
        if response.status_code == 200:
            pass
        else:
            utils.printStatus(response.status_code)

    def put(self, localFileName, hdfsFileName):
        if (os.system(f"test -d {localFileName}") == 0):
            print(f"'{localFileName}' is a directory")
            return
        if (os.system(f"test -f {localFileName}") != 0):
            print(f"'{localFileName}' no such file")
            return
        
        data = open(localFileName, "r").read
        response = requests.put(f"{self.home}{self.current_path}{hdfsFileName}",
                                params={"user.name": self.user,
                                        "op": "CREATE",
                                        "overwrite": "true"})
        url = response.url
        response = requests.put(url=url, data=data())
        if response.status_code == 201:
            pass
        else:
            utils.printStatus(response.status_code)
    
    def get(self, hdfsFileName, localFileName):
        if (os.system(f"test -d {localFileName}") == 0):
            print(f"'{localFileName}' is a directory")
            return

        response = requests.get(f"{self.home}{self.current_path}{hdfsFileName}?op=OPEN")
        if response.status_code != 200:
            utils.printStatus(response.status_code)
            return
        url = response.url
        response = requests.get(url)
        with open(localFileName, 'wb') as file:
            file.write(response.content)
        

    def append(self, localFileName, hdfsFileName):
        if (os.system(f"test -d {localFileName}") == 0):
            print(f"'{localFileName}' is a directory")
            return
        if (os.system(f"test -f {localFileName}") != 0):
            print(f"'{localFileName}' no such file")
            return

        data = open(self.local_current_path + localFileName, "r").read
        response = requests.post(f"{self.home}{self.current_path}{hdfsFileName}",
                                 params={"user.name": self.user,
                                         "op": "APPEND"})
        url = response.url
        response = requests.post(url=url, data=data())
        if response.status_code == 200:
            pass
        else:
            utils.printStatus(response.status_code)

    def delete(self, fileName):
        response = requests.delete(f"{self.home}{self.current_path}{fileName}",
                                   params={"user.name": self.user,
                                           "op": "DELETE"})

        if response.status_code == 200:
            pass
        else:
            utils.printStatus(response.status_code)

    def ls(self):
        response = requests.get(f"{self.home}{self.current_path}",
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

        for directory in directories:
            print("[d] "+ directory)
        for file in files:
            print("[f] "+ file)

    def cd(self, path):
        newPath = utils.constructPath(self.current_path, path)
        response = requests.get(f"{self.home}{newPath}?op=GETFILESTATUS")
        if response.status_code == 200:
            self.current_path = newPath
        elif response.status_code == 404:
            print("Directory not found")
        else:
            utils.printStatus(response.status_code)

    def lls(self):
        os.system(f"ls {self.local_current_path}")

    def lcd(self, path):
        newPath = utils.constructPath(self.local_current_path, path)
        status = os.system(f"test -d {newPath}")
        if status == 0:
            self.local_current_path = newPath
        else:
            print("Directory not found")

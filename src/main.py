import sys
import hcmd
import client

def main():

    if len(sys.argv) != 4:
        print("hdfscli [host] [port] [user]")
        return
    
    host, port, user = sys.argv[1:4]
    hdfs = client.HDFS(host, port, user)
    
    print(f'Connected to {user}@{host}:{port}')
    
    while True:
        cmd = input(f"[{user}][H:{hdfs.current_path}][L:{hdfs.local_current_path}] $ ")
        hcmd.exec(hdfs, cmd)


if __name__ == "__main__":
    main()

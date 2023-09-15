import sys
import parse_cmd

if len(sys.argv) < 4:
    print("Enter the required arguments")
    sys.exit()
elif len(sys.argv) > 4:
    print("Lots of arguments")

HOST, PORT, USER = sys.argv[1:4]


def main():
    print(HOST, PORT, USER)
    while True:
        cmd = input(f"[HDFS_client_{USER}]$: ")
        parse_cmd.parse_cmd(cmd)


if __name__ == "__main__":
    main()

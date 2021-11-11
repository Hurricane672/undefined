import os


def start_proxy():

    command = 'mitmdump --listen-host 127.0.0.1 -p 8081 -s catch.py'
    os.system(command)


if __name__ == "__main__":
    start_proxy()



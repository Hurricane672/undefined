from threading import Thread
import os
import time

def start_proxy():
    command = 'mitmdump --listen-host 127.0.0.1 -p 8081 -s catch.py'
    os.system(command)


if __name__ == '__main__':
    t = Thread(target=start_proxy)
    t.daemon = True
    t.start()
    time.sleep(7)
    input()
    os.system('taskkill /F /IM "mitmdump.exe" >> output.log 2>&1')
    os.system("del output.log")
    print(1)
from multiprocessing import Process
import os
import time


def start_proxy():
    command = 'mitmdump --listen-host 127.0.0.1 -p 8081 -s ./lib/catch.py'
    os.system(command)


def main():
    print("[1] PREPARING processing started")
    print("[*] RECORDER started")
    print("[*] Now you can start your explore of the target URL")
    print("[*] Proxy server started")
    print("[*] Open the browser and shift the http proxy to 127.0.0.1:8081")
    processes = []
    t1 = Process(target=start_proxy)
    t1.daemon = True
    t1.start()
    flag = 1
    print("    Press any key to quit the recording process: ")
    while input() != "":
        continue
    t1.kill()
    print("[*] RECORDER has been stop")
    print("[*] The result has been written to ./lib/outfile.txt")
    # processes.append(t1)
    # for t in processes:
    #     t.daemon = False
    #     t.start()


if __name__ == '__main__':
    main()

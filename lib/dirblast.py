import requests
import tqdm
from multiprocessing import Process
from threading import Thread

global dir_list, file_list
dir_list = []


def scanDir(dir_list):
    url0 = "http://192.168.1.101/"
    # found_lists = []
    # note_lists = []
    for i in tqdm.tqdm(dir_list):
        url = url0 + i[:-1]
        r = requests.get(url)
        if r.status_code == 404:
            pass
        elif r.status_code == 403:
            print("[*] Directory " + url + " found")
        else:
            print("[!] The url " + url + " has met the status code *" + str(r.status_code) + "*")
    return


def main():
    f = open("../wordlists/dir/dir6.txt")
    l = f.readlines()
    processes = []
    num = int(len(l) / 2)
    t1 = Process(target=scanDir, args=(l[:num]))
    t2 = Process(target=scanDir, args=[l[num:]])
    processes.append(t1)
    processes.append(t2)
    for t in processes:
        t.daemon = False
        t.start()


if __name__ == "__main__":
    main()
    # for i in found_lists:
    #    print(i)
    # for i in note_lists:
    #    print(i)

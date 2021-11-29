"""
    ___              __         ______
   /   |  ____  ____/ /_  __   / ____/_  ______
  / /| | / __ \/ __  / / / /  / /_  / / / / __ \
 / ___ |/ / / / /_/ / /_/ /  / __/ / /_/ / / / /
/_/  |_/_/ /_/\__,_/\__, /  /_/    \__,_/_/ /_/
                   /____/
ERROR Code:
1-SQLMap server disconnected
2-Add new task failed
"""

from threading import Thread
from time import sleep
from terminaltables import AsciiTable as atb
from os import system
import requests
import json

animation = "|/-\\"
title = '''
    ___              __         ______
   /   |  ____  ____/ /_  __   / ____/_  ______
  / /| | / __ \/ __  / / / /  / /_  / / / / __ \\
 / ___ |/ / / / /_/ / /_/ /  / __/ / /_/ / / / /
/_/  |_/_/ /_/\__,_/\__, /  /_/    \__,_/_/ /_/
                   /____/  '''


class SQLTask:
    headers = {'content-type': 'application/json'}
    id = ""
    url = "http://127.0.0.1:8775/"
    target = ""
    parameter = {}

    def __init__(self, target, level, method="GET", body=None):
        if body is None:
            body = {}
        self.parameter = {'url': target, "level": level}
        self.parameter = {'url': target}
        print("[*] Creating SQL Task for the target " + target)
        try:
            response = json.loads(requests.get(self.url + "task/new").text)
        except requests.exceptions.ConnectionError:
            print("[!] SQLMap server disconnected")
            exit(1)
        else:
            self.id = response["taskid"]
            self.target = target
            if not response["success"]:
                print("[!] Add new task failed")
                exit(2)
            else:
                print("[#] Task added successfully")
                print(atb([["Target", "ID"], [self.target, self.id]]).table)
                # print(atb([["Target", "ID"], [self.target, self.id]]).table)

    def start(self):
        print("[*] Start scanning")
        response = json.loads(requests.post(self.url + "scan/" + self.id + "/start", data=json.dumps(self.parameter),
                                            headers=self.headers).text)
        if response["success"]:
            print("[*] The engine id is " + str(response["engineid"]))

    def status(self):
        response = json.loads(requests.get(self.url + "scan/" + self.id + "/status").text)
        if response["success"]:
            if response["status"] == "running":
                # print("The task "+self.id+" is still running")
                return 1
            elif response["status"] == "terminated":
                print("[#] The task " + self.id + " has been already terminated")
                return 0
            else:
                print("[!] Something went wrong")
                return -1
        else:
            print("[!] Something went wrong")
            exit(-1)

    def data(self):
        response = json.loads(requests.get(self.url + "scan/" + self.id + "/data").text)
        if response["success"]:
            print("------------------------DATA------------------------")
            print(response["data"])
            print("------------------------DATA------------------------")
            return response
        else:
            print("[!] Something went wrong")
            exit(-1)

    def close(self):
        response = json.loads(requests.get(self.url + "scan/" + self.id + "/kill").text)
        # print(response)
        if response["success"]:
            print("[#] The task " + self.id + " killed")
        else:
            print("[#] The task " + self.id + " has already closed")


def open_SQLMapServer():
    command = "python ../sqlmap/sqlmapapi.py -s >> temp.log 2>&1"
    system(command)


def scan(url, level):
    task1 = SQLTask(url, level)
    task1.start()
    task1.status()
    print("[*] The task is still running")
    while task1.status():
        #print(task1.status())
        sleep(0.1)
    data = task1.data()
    # ["title","payload","where","vector","comment","templatePayload","matchRation","trueCode","falseCode"]
    data_head = ["title", "payload", "where", "vector"]
    data_list = []
    print(data["data"][1]["value"][0]["data"].values())
    for i in data["data"][1]["value"][0]["data"].values():
        data_list.append(list(i.values())[0:4])
    # print(atb(data_list).table)
    c = 1
    for i in data_list:
        print(str(c))
        for j in range(0, len(i)):
            print("+ " + data_head[j] + " : " + str(i[j]))
        c += 1
    task1.close()
    return data


def main():
    threads = []
    url = u"http://10.122.199.187:82/Less-1?id="
    level = u"2"
    t1 = Thread(target=open_SQLMapServer)
    threads.append(t1)
    t2 = Thread(target=scan, args=(url, level))
    threads.append(t2)
    t1.daemon = True
    t2.daemon = False
    t1.start()
    sleep(2)
    t2.start()


if __name__ == '__main__':
    main()

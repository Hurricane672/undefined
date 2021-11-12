from multiprocessing import Process
import os
import json
from terminaltables import AsciiTable
import requests
import re

animation = "|/-\\"


def getUrl(url, root, urls):
    reg = re.compile('(?<=href=")[^"]*(?=")')
    page = requests.get(url)
    response_text = page.content.decode("utf-8")
    r1 = re.findall(reg, response_text)
    r2 = []
    for r in r1:
        if "http://" not in r and "https://" not in r:
            if r[-3:] == "css" or r[0] == "#":
                continue
            else:
                if (url == root) and (url + r not in r2) and (url + r not in urls):
                    r2.append(url + r)
                elif (url != root) and (url[-4] != "." and url[-5] != "." and url[-6] != ".") and (
                        url + "/" + r not in r2) and (url + "/" + r not in urls):
                    r2.append(url + "/" + r)
                elif (url != root) and (url[-4] == "." or url[-5] == "." or url[-6] == ".") and (
                        url + "/" + r not in r2) and (url + "/" + r not in urls):
                    s = "/".join(url.split("/")[:-1]) + "/" + r
                    if s not in r2 and s not in urls:
                        r2.append(s)
                else:
                    pass
        else:
            pass
    return r2


def urlNotInParametersList(url_check, urls, parameters):
    if url_check not in urls:
        for i in urls:
            if (url_check.split("?")[0] in i.split("?")[0] or i.split("?")[0] in url_check.split("?")[0]) and \
                    url_check.split("?")[1] == \
                    i.split("?")[1]:
                parameters.append(url_check.split("?")[1])
                return False
        return True
    else:
        return False


def urlNotInNoParametersList(url_check, urls):
    if url_check[-1] != "/":
        url_check += "/"
    else:
        pass
    if url_check not in urls:
        for i in urls:
            if url_check == i:
                return False
        return True
    else:
        return False


def collect():
    urls_with_params = []
    urls_without_params = []
    parameters = []
    cookies = []
    headers = []
    file = open("./lib/outfile.txt", "r+", encoding="utf-8")
    for i in file.readlines():
        dic = json.loads(i)
        if dic["action"] == "request":
            if "?" in dic["url"] and urlNotInParametersList(dic["url"], urls_with_params, parameters):
                urls_with_params.append(dic["url"])
            elif "?" not in dic["url"] and urlNotInNoParametersList(dic["url"], urls_without_params):
                urls_without_params.append(dic["url"])
            else:
                pass
            if dic["headers"] not in headers and dic["headers"] != {}:
                headers.append(dic["headers"])
            if dic["cookies"] not in cookies and dic["cookies"] != {}:
                cookies.append(dic["cookies"])
    return urls_without_params, urls_with_params, parameters, cookies, headers


def start_proxy():
    command = 'mitmdump --listen-host 127.0.0.1 -p 8081 -s ./lib/catch.py'
    os.system(command)


def dirBlast():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BLAST~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("[*] BLAST scan start")


def main(root):
    print("----------------------------PREPARING----------------------------")
    ##############################################################################
    ext = ""
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PASSIVE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("[*] PASSIVE scan part")
    print("[*] RECORDER started")
    print("[*] Now you can start your explore of the target URL")
    print("[*] Proxy server started")
    # print("[*] Open the browser and shift the http proxy to 127.0.0.1:8081")
    # processes = []
    # t1 = Process(target=start_proxy)
    # t1.daemon = True
    # t1.start()
    # print("    Press any key to quit the recording process: ")
    # while input() != "":
    #     time.sleep(1)
    #     continue
    # t1.terminate()
    # os.system('taskkill /F /IM "mitmdump.exe" >> temp.log 2>&1')
    # os.system("del temp.log")
    print("[*] RECORDER has been stop")
    print("[*] The result has been written to ./lib/outfile.txt")
    print("[*] Collecting requests")
    urls_without_params, urls_with_params, parameters, cookies, headers = collect()
    print("[*] Follows info are found: ")
    print(AsciiTable([["URLs without parameters"], ["\n".join(urls_without_params)]]).table)
    print(AsciiTable([["URLs with parameters"], ["\n".join(urls_with_params)]]).table)
    print(AsciiTable([["Parameters"], ["\n".join(parameters)]]).table)
    print("Cookie list:")
    for i in cookies:
        print(i)
    ##############################################################################
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~RECURSIVE~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("[*] ACTIVE scan part")
    print("[*] RECURSIVE scan start")
    expected_extensions = [".php", ".asp", ".py"]
    urls = [root]
    root = root
    for i in urls:
        urls += getUrl(i, root, urls)
    for i in urls:
        for e in expected_extensions or ext == "":
            if e in i:
                ext = e
        if urlNotInNoParametersList(i, urls_without_params):
            urls_without_params.append(i)
        else:
            pass
    print("[*] URLs without parameters is now updated to:")
    print(AsciiTable([["URLs without parameters"], ["\n".join(urls_without_params)]]).table)
    if ext != "":
        print("[+] Language " + ext[1:] + " found")
        print("[!] ext=" + ext)
    else:
        print("[*] Unknown language")
        print("[!] ext=EMPTY")
    ext1 = input("[?] Would you like to change the file extension? ")
    if ext1 != "":
        ext = ext1
    else:
        pass
    print("ext=" + ext)
    ##############################################################################
    ans = input("[?] Would you like to do the BLASTING scan?(y/n)")
    if ans == "y":
        dirBlast()
    else:
        pass
    ##############################################################################
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CHECK~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in urls_without_params:
        print("[*] Check the url " + i)
        response = requests.get(i)
        if response.status_code == 404:
            print("[!] The url " + i + " has no response which will be delete")
            urls_without_params.remove(i)
        else:
            print("OK")
            continue
    for i in urls_with_params:
        print("[*] Check the url " + i)
        response = requests.get(i)
        if response.status_code == 404:
            print("[!] The url " + i + " has no response which will be delete")
            urls_with_params.remove(i)
        else:
            print("OK")
            continue
    print("[*] Check completed")
    print("[*] Prepare completed")
    # for i in range(0, len(urls_without_params)):
    #     response = requests.get(urls_without_params[i])
    #     if response.status_code == 404:
    #         del urls_without_params[i]
    #     else:
    #         continue
    # for i in range(0, len(urls_with_params)):
    #     response = requests.get(urls_with_params[i])
    #     if response.status_code == 404:
    #         del urls_with_params[i]
    #     else:
    #         continue
    return urls_without_params, urls_with_params, parameters, cookies, headers


if __name__ == '__main__':
    main("")

import os
import json
from terminaltables import AsciiTable
import requests
import re


def getUrl(url, root, urls):
    reg = re.compile('(?<=href=")[^"]*(?=")')
    # reg2 = re.compile('[^/]*html')
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
                # if re.search(reg2, url):
                #     print(url)
                #     n = re.sub(reg2, "", url)
                #     n += r
                #     print(n)
                #     if n not in urls and n not in r2:
                #         r2.append(n)
                # else:
                #     if url != root:
                #         url += "/"
                #         url += r
                #         if url not in urls and url not in r2:
                #             r2.append(url)
                #     else:
                #         url += r
                #         if url not in urls and url not in r2:
                #             r2.append(url)
        else:
            pass
    return r2


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


def main():
    root = "http://10.122.199.187:82/"
    urls_without_params = []
    ext = ""
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~RECURSIVE~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("[*] ACTIVE scan part")
    print("[*] RECURSIVE scan start")
    expected_extensions = [".php", ".asp", ".py"]
    urls = [root]
    for i in urls:
        urls += getUrl(i, root, urls)
        # print(urls)
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


if __name__ == "__main__":
    main()

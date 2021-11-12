import re
import requests
import json
from progressbar import progressbar

# def get_href(url, path):
#     file = open(path + ".json", "w+", encoding="utf-8")
#     reg = re.compile('(?<=href=")[^"]*(?=")')
#     page = requests.get(url)
#     response_text = page.content.decode("utf-8")
#     url_list = re.findall(reg, response_text)
#     file.write(json.dumps(url_list))
#
#
# add = "http://"
# root = '127.0.0.1'
# path = "/"
# target = add + root + path
# directory = root + path
# page = requests.get(target)
# file = open("index.json", "r+", encoding="utf-8")
# urls = json.loads(file.read())
# for url in urls:
#     get_href(target + url, directory + url)


def get_url(url, root, urls):
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
                if root + r not in urls and root + r not in r2:
                    r2.append(root + r)
        else:
            pass
    return r2

if __name__ == "__main__":
    extensions_expected = [".php",".asp",".py"]
    urls = ["http://10.122.199.187/"]
    root = "http://10.122.199.187/"
    # urls = ["http://192.168.64.129/"]
    # root = "http://192.168.64.129/"
    i = 0
    while i < len(urls):
        urls += get_url(urls[i], root, urls)
        i += 1
    ext = ""
    for url in urls:
        for e in extensions_expected or ext=="":
            if e in url:
                ext = e
        print(url)
    if ext!="":
        print("[?] Language "+ext[1:]+" found")
    else:
        print("[*] Unknown language")
    # reg = re.compile('(?<=<script src=")[^"]*(?=">)')

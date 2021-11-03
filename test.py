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
        if r[-3:] == "css" or r[0] == "#":
            continue
            # print(r)
        else:
            if root + r not in urls and root + r not in r2:
                r2.append(root + r)
    return r2


if __name__ == "__main__":
    urls = ["http://127.0.0.1/"]
    root = "http://127.0.0.1/"
    # urls = ["http://192.168.64.129/"]
    # root = "http://192.168.64.129/"
    i = 0
    while i < len(urls):
        urls += get_url(urls[i], root, urls)
        i += 1
        print(str(i) + "/" + str(len(urls)))

    file = open("urls1.json", "w+", encoding="utf-8")
    file.write(json.dumps(urls))
    # reg = re.compile('(?<=<script src=")[^"]*(?=">)')

import requests as re
import re as r


def getJSList(url, proxies):
    response = re.get(url, proxies=proxies)
    reg = r.compile('(?<=<script src=")[^"]*(?=">)')
    response_text = response.content.decode("utf-8")
    js_list = r.findall(reg, response_text)
    return js_list


# def getJS():
#     url1 = url + l[0]
#     print(url1)
#     response1 = re.get(url1, proxies=proxies)
#     print(response1.text)

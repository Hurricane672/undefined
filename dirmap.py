import requests
import re


def getPage(url,path):
    open(path+"")

def getJSList(url):
    response = requests.get(url)
    reg = re.compile('(?<=<script src=")[^"]*(?=">)')
    response_text = response.content.decode("utf-8")
    js_list = re.findall(reg, response_text)
    return js_list

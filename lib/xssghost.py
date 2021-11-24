# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import sys

from selenium.webdriver.common import service


def phadsys():
    if sys.platform.startswith('win'):
        return "./thirdparty/chrome/chromedriver-win.exe"
    elif sys.platform.startswith('linux'):
        return "./thirdparty/chrome/chromedriver-linux"
    else:
        print("unsupportable system")
        sys.exit(0)


def driver_settings():
    chrome_opt = webdriver.ChromeOptions()

    # chrome_opt.add_argument('--headless')
    chrome_opt.add_argument('--disable-gpu')
    chrome_opt.add_argument(
        '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"')

    return chrome_opt


def main():
    server = Service(phadsys())
    target = []
    submitbtn = []
    payload="test"
    Ourl = 'https://www.baidu.com'
    driver = webdriver.Chrome(service=server, options=driver_settings())
    driver.implicitly_wait(10)

    driver.get(Ourl)
    inputers = driver.find_elements_by_xpath("//input")
    for inpu in inputers[:]:
        nowtype = inpu.get_attribute("type")
        if nowtype == "hidden":
            inputers.remove(inpu)
        elif nowtype == "text" or nowtype == "password":
            target.append(inpu)
        elif nowtype == "submit":
            submitbtn.append(inpu)

    for attck in target:
        attck.send_keys(payload+Keys.ENTER)
    for inpu in submitbtn:
        print(inpu.get_attribute("type"))

    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()

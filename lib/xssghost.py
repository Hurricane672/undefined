from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import sys

from selenium.webdriver.common import service

def phadsys():
    if sys.platform.startswith('win'):
        return "D:/experimentalClass/AndyFUN/thirdparty/chrome/chromedriver-win.exe"
    elif sys.platform.startswith('linux'):
        return "./thirdparty/chrome/chromedriver-linux"
    else:
        print("unsupportable system")
        sys.exit(0)


def main():
    s=Service(phadsys())
    driver = webdriver.Chrome(service=s)
    driver.get("https://www.bilibili.com/")
    driver.get_screenshot_as_file("C:\\Users\\HP\\Desktop\\biili.png")
    driver.quit()


if __name__ == '__main__':
    main()

#coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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
    
    chrome_opt.add_argument('--headless')
    chrome_opt.add_argument('--disable-gpu')
    chrome_opt.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"')
    
    
    return chrome_opt

def main():
    server = Service(phadsys())

    driver = webdriver.Chrome(service=server,options=driver_settings())
    driver.implicitly_wait(10) 

    driver.get('https://www.baidu.com')
    print("\n"+driver.title)
    
    driver.quit()
   

if __name__ == '__main__':
    main()

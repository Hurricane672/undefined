from selenium import webdriver
import time
import sys

def phadsys():
    if sys.platform.startswith('win'):
        return "./thirdparty/phantomjs/Windows/phantomjs.exe"
    elif sys.platform.startswith('linux'):
        return "./thirdparty/phantomjs/Linux/phantomjs"
    else:
        print("unsupportable system")
        sys.exit(0)


def main():
    driver = webdriver.PhantomJS(executable_path=phadsys())
    driver.get("https://www.bilibili.com/")
    driver.get_screenshot_as_file("C:\\Users\\HP\\Desktop\\biili.png")


if __name__ == '__main__':
    main()

import os
from lib import prepare
from lib import SQLInject
from terminaltables import AsciiTable
import json
import time
from lib import xssghost

title = '''
    ___              __         ______
   /   |  ____  ____/ /_  __   / ____/_  ______
  / /| | / __ \/ __  / / / /  / /_  / / / / __ \\
 / ___ |/ / / / /_/ / /_/ /  / __/ / /_/ / / / /
/_/  |_/_/ /_/\__,_/\__, /  /_/    \__,_/_/ /_/
                   /____/  '''


# def init(target):
#     print("Making directory ./"+target+"/")
#     if not os.path.exists(target):
#         os.mkdir(target)
#         print("Done")
#     else:
#         print("Directory already exists.")
#     return target

def main():
    report = open("report.txt", "w+", encoding="utf-8")
    report_title = "**REPORT**"
    report.write(report_title)
    report.write("\n")
    report.write(time.asctime(time.localtime(time.time())))
    report.write("\n")
    print(title)
    print("Thanks for using Andy Fun Scanner.")
    # url = input("Input the URL to scan: ")
    url = "http://10.122.199.187:82/"
    print("[+] URL " + url + " got")
    print("==============================START==============================")
    # prepare.main()
    urls_without_params, urls_with_params, parameters, cookies, headers, body, post_list, ext = prepare.main(url)
    print("Writing in to report.txt")
    report.write("1. Preparation\n")
    report.write("Followings has been detected\n")
    report.write(AsciiTable([["URLs without parameters"], ["\n".join(urls_without_params)]]).table)
    report.write("\n")
    report.write(AsciiTable([["URLs with parameters"], ["\n".join(urls_with_params)]]).table)
    report.write("\n")
    print("done")
    SQLInject.main(urls_without_params, urls_with_params, parameters, cookies, headers, body, post_list, ext, url)
    print("===============================END===============================")
    report.close()
    # xssghost.main()

if __name__ == '__main__':
    main()

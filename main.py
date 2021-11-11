import os
from lib import prepare

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
    print(title)
    print("Thanks for using Andy Fun Scanner.")
    url = input("Input the URL to scan: ")
    url = "http://10.122.199.187"
    print("[+] URL " + url + " got")
    print("==============================START==============================")
    prepare.main()
    print("===============================END===============================")


if __name__ == '__main__':
    main()

import requests
import os
from progressbar import *
import time
import dirmap
title = '''
    ___              __         ______
   /   |  ____  ____/ /_  __   / ____/_  ______
  / /| | / __ \/ __  / / / /  / /_  / / / / __ \\
 / ___ |/ / / / /_/ / /_/ /  / __/ / /_/ / / / /
/_/  |_/_/ /_/\__,_/\__, /  /_/    \__,_/_/ /_/
                   /____/  '''

def init(target):
    print("Making directory ./"+target+"/")
    if not os.path.exists(target):
        os.mkdir(target)
        print("Done")
    else:
        print("Directory already exists.")
    return target


if __name__ == '__main__':
    target = init(input("Enter the url to start scan: "))
    dirmap.getJSList(target)

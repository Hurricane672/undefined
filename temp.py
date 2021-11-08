
import random
import time
from tqdm import tqdm

fi = open("./wordlists/dir/directory-list-2.3-small.txt","r+")
fo = open("./wordlists/dir/dirsadd.txt","w+")
l0 = fi.readlines()
l1 = []
for i in l0:
    l1.append("/"+i)
fo.writelines(l1)
fi.close()
fo.close()

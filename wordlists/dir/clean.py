from tqdm import tqdm


def clean1(l0):
    l1 = []
    for i in tqdm(l0):
        if "." in i:
            pass
        else:
            l1.append(i)
    return l1


def clean2(l0):
    l1 = []
    for i in tqdm(l0):
        if i[-2] == "/":
            l1.append(i[:-2]+"\n")
        else:
            l1.append(i)
    return l1


def clean3(l0):
    l1 = []
    for i in tqdm(l0):
        if "{ext}" in i:
            pass
        else:
            l1.append(i)
    return l1


def clean4(l0):
    l1 = []
    for i in tqdm(l0):
        if i in l1:
            pass
        else:
            l1.append(i)
    return l1


def main():
    fi = open("dir5.txt", "r+")
    fi2 = open("dirsadd.txt", "r+")
    fo = open("dir6.txt", "w+")
    # fo.writelines(clean4(clean3(clean2(clean1(fi.readlines())))))
    fo.writelines(clean4(fi.readlines()+fi2.readlines()))
    fi.close()
    fi2.close()
    fo.close()


if __name__ == "__main__":
    main()

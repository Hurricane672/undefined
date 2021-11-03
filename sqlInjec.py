import subprocess


def convert(b):
    return str(b, encoding='gb2312')


# command = "python ./sqlmap/sqlmap.py -u \"127.0.0.1/Less-1?id=1\""
# command = "chcp 65001"
# # command = "dir"
pro = subprocess.Popen("python ./sqlmap/sqlmapapi.py -c ; new -u \"http://192.168.64.129\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
# pro.stdin.write(b'chcp 65001\n')
# pro.stdin.write(b"echo 1111111111111\n")
# pro.stdin.write(b"echo 1121111111111\n")
# print(convert(pro.stdout.read()))
# pro.communicate()
# print(pro.communicate(""))
print(convert(pro.stdout.read()))
# pro.stdin.write(b"dir\n")
# print(convert(pro.stdout.read()))
# print(convert(out))
# print(convert(err))
# print(pro.stdout.readlines())
# print(convert(pro.stdout.read()))

# pro = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
# for i in pro.stdout.readline,'b':
#     print(str(i).replace("\\r\\n",""))
# for i in iter(pro.stdout.readline, 'b'):
#     print(str(i).replace("\\r\\n", ""))
# print(pro.stdout.read())

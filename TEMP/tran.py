import json


def jsonizeHeaders(headers):
    return json.loads(
        headers["headers"][7:].replace("b'", "'").replace("), (", "???").replace(",", ":").replace("[(", "{").replace(
            ")]", "}").replace("???", ",").replace("\"", "").replace("'", "\""))


def jsonizeCookies(cookies):
    if cookies=="MultiDictView[]":
        d = {}
        return d
    else:
        r = cookies.replace("MultiDictView", "").replace("[[","{").replace("]]","}").replace("', '","\":\"").replace("], [",",").replace("'","\"")
        print(r)
        return json.loads(r)


f = open("outfile.txt", "r", encoding="utf-8")
for i in f.readlines():
    print(json.loads(i))
# headers = jsonizeHeaders(dic)
# print(headers)

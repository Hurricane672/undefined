from mitmproxy import ctx
import json


def jsonizeHeaders(headers):
    return json.loads(
        headers[7:].replace("b'", "'").replace("), (", "???").replace(",", ":").replace("[(", "{").replace(
            ")]", "}").replace("???", ",").replace("\"", "").replace("'", "\""))


def jsonizeCookies(cookies):
    if cookies == "MultiDictView[]":
        d = {}
        return d
    else:
        s = cookies.replace("MultiDictView", "").replace("[[", "{").replace("]]", "}").replace("', '", "\":\"").replace(
            "], [", ",").replace("'", "\"")
        try:
            r = json.loads(s)
            return r
        except:
            d = {}
            return d


def request(flow):
    """
     {'action':str,'method':str,'url':str,'host':str,'port':str,'headers':dict,'cookies':dict(,'body':str)}
    """
    request = flow.request
    info = ctx.log.info
    url = request.url
    if ("js" not in url) and ("jpg" not in url) and ("png" not in url) and ("css" not in url):
        f = open("outfile.txt", "a+", encoding="utf-8")
        request_list = {"action": "request"}
        info("[<] " + request.url)  # 打印请求的url
        request_list["method"] = str(request.method)
        request_list["url"] = str(request.url)
        request_list["host"] = str(request.host)
        request_list["port"] = str(request.port)
        request_list["headers"] = jsonizeHeaders(str(request.headers))
        request_list["cookies"] = jsonizeCookies(str(request.cookies))
        if str(request.method) == "POST":
            try:
                request_list["body"] = str(request.postBody)
            except:
                pass
        f.write(json.dumps(request_list))
        f.write("\n")
        f.close()
    else:
        pass


def response(flow):
    """
     {'action':str,'code':str,'headers':str,'cookies':str,'body':str}
    """
    response = flow.response
    info = ctx.log.info
    if response.status_code != 302:
        f = open("outfile.txt", "a+", encoding="utf-8")
        response_list = {"action": "response"}
        # info(str("[>] " + str(response.status_code)))
        response_list["code"] = str(response.status_code)
        response_list["headers"] = jsonizeHeaders(str(response.headers))
        response_list["cookies"] = jsonizeCookies(str(response.cookies))
        response_list["body"] = str(response.text)
        f.write(json.dumps(response_list))
        f.write("\n")
    else:
        pass

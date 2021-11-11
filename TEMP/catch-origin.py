from mitmproxy import ctx


# 所有发出的请求数据包都会被这个方法所处理
# 所谓的处理，我们这里只是打印一下一些项；当然可以修改这些项的值直接给这些项赋值即可
def request(flow):
    request = flow.request  # 获取请求对象
    info = ctx.log.info  # 实例化输出类
    url = request.url
    if("js" not in url) or ("jpg" not in url) or ("png" not in url) or ("css" not in url):
        f = open("../outfile.txt", "a+", encoding="utf-8")
        request_list = ["request"]
        f.write("================REQUEST================\n")
        info(request.url)  # 打印请求的url
        f.write(str(request.url) + "\n")
        # info(request.method)  # 打印请求方法
        f.write(str(request.method) + "\n")
        # info(request.host)  # 打印host头
        f.write(request.host + "\n")
        # info(str(request.port))  # 打印请求端口
        f.write(str(request.port) + "\n")
        # info(str(request.headers))  # 打印所有请求头部
        f.write(str(request.headers) + "\n")
        #info(str(request.cookies))  # 打印cookie头
        f.write(str(request.cookies) + "\n")
        if str(request.method) == "POST":
            try:
                # info(str(request.postBody))
                f.write(str(request.postBody) + "\n")
            except:
                pass
        f.write("================REQUEST================\n")
        f.write("\n")
        f.close()
    else:
        pass


# 所有服务器响应的数据包都会被这个方法处理
# 所谓的处理，我们这里只是打印一下一些项
def response(flow):
    response = flow.response  # 获取响应对象
    info = ctx.log.info  # 实例化输出类
    # if("js" in url) or ("jpg" in url) or ("png" in url):
    #     exit()
    if response.status_code != 304:
        f = open("../outfile.txt", "a+", encoding="utf-8")
        f.write("================RESPONSE================\n")
        # info(str(response.status_code))  # 打印响应码
        f.write(str(response.status_code) + "\n")
        # info(str(response.headers))  # 打印所有头部
        f.write(str(response.headers) + "\n")
        # info(str(response.cookies))  # 打印cookie头部
        f.write(str(response.cookies) + "\n")
        # info(str(response.text))  # 打印响应报文内容
        f.write(str(response.text) + "\n")
        f.write("================RESPONSE================\n")
        f.write("\n")
    else:
        pass

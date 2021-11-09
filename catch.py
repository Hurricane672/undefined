from mitmproxy import ctx


# 所有发出的请求数据包都会被这个方法所处理
# 所谓的处理，我们这里只是打印一下一些项；当然可以修改这些项的值直接给这些项赋值即可
def request(flow):
    f = open("../outfile.txt", "a+")
    f.write("================REQUEST================")
    request = flow.request  # 获取请求对象
    info = ctx.log.info  # 实例化输出类
    info(request.url)  # 打印请求的url
    f.write(str(request.url) + "\n")
    info(request.method)  # 打印请求方法
    f.write(str(request.method) + "\n")
    info(request.host)  # 打印host头
    f.write(request.host + "\n")
    info(str(request.port))  # 打印请求端口
    f.write(str(request.port) + "\n")
    info(str(request.headers))  # 打印所有请求头部
    f.write(str(request.headers) + "\n")  # 打印cookie头
    info(str(request.cookies))
    f.write(str(request.cookies))
    f.write("================REQUEST================")
    f.write("\n")
    f.close()


# 所有服务器响应的数据包都会被这个方法处理
# 所谓的处理，我们这里只是打印一下一些项
def response(flow):
    f = open("../outfile.txt", "a+")
    f.write("================RESPONSE================")
    response = flow.response  # 获取响应对象
    info = ctx.log.info  # 实例化输出类
    info(str(response.status_code))  # 打印响应码
    f.write(str(response.status_code) + "\n")
    info(str(response.headers))  # 打印所有头部
    f.write(str(response.headers) + "\n")
    info(str(response.cookies))  # 打印cookie头部
    f.write(str(response.cookies) + "\n")
    info(str(response.text))  # 打印响应报文内容
    f.write(str(response.text) + "\n")
    f.write("================RESPONSE================")
    f.write("\n")

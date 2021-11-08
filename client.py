import asyncio, pproxy


async def test_tcp(proxy_uri):
    conn = pproxy.Connection(proxy_uri)
    reader, writer = await conn.tcp_connect('www.baidu.com', 80)
    writer.write(b'GET / HTTP/1.1\r\n\r\n')
    data = await reader.read(1024 * 16)
    print(data.decode())


asyncio.run(test_tcp('http://127.0.0.1:8888'))

import socket
import re

PROXY_PORT = 1080
bufsize = 65536


class Server:
    def __init__(self, sock=None):
        self.socket = sock

    def recv_all_data(self, from_client=False):
        """
        :param from_client:
            当接收客户端请求的时候,如果是post，就会有Content-Length，防止过长
            如果是get的话，结尾就是\r\n\r\n
        :return:
        """
        sock = self.socket
        data = sock.recv(bufsize)
        if b'Content-Length' in data:  # 数据没压缩的时候，以Content-Length判断数据是否传输结束
            length = re.search(r'Content-Length: (\d+)', data.decode(encoding='utf8')).group(1)
            head_length = len(data.split(b'\r\n\r\n')[0]) + 4
            total = int(length) + head_length  # 响应头+内容长度 = 总长度
            while len(data) != total:
                data += sock.recv(bufsize)
        else:  # 数据压缩传输的时候，以b'\r\n0\r\n\r\n'判断是否传输结束 或者 from_client=Ture 方法是get的时候
            condition = b'\r\n\r\n' if from_client else b'\r\n0\r\n\r\n'
            while data[-len(condition):] != condition:
                data += sock.recv(bufsize)
        return data

    @staticmethod
    def get_host_port(data: bytes):
        data = data.decode(encoding='utf8')
        if 'http://' in data:
            host = data.split('\r\n')[1].split()[1]
            port = 80
        else:
            host = re.search(r'\s([^\s]+):443', data).group(1)
            port = 443

        return host, port

    @classmethod
    def get_web_data(cls, addr, _send_data):
        sender = socket.socket()
        sender.connect(addr)
        sender.sendall(_send_data)
        result = cls(sender).recv_all_data()
        sender.close()
        return result


if __name__ == '__main__':
    server = socket.socket()
    server.bind(('0.0.0.0', PROXY_PORT))
    server.listen(1024)
    while True:
        origin_conn, origin_addr = server.accept()
        send_data = Server(origin_conn).recv_all_data(from_client=True)
        target_addr = Server.get_host_port(send_data)
        result_data = Server.get_web_data(target_addr, send_data)
        origin_conn.sendall(result_data)
        origin_conn.close()
    server.close()
    print('end')
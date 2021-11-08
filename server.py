import asyncio
import pproxy

server = pproxy.Server('http://127.0.0.1:8888')
remote = pproxy.Connection('http://127.0.0.1:8080')
args = dict(rserver=[remote],verbose=print)

loop = asyncio.get_event_loop()
handler = loop.run_until_complete(server.start_server(args))
try:
    loop.run_forever()
except KeyboardInterrupt:
    print('exit!')

handler.close()
loop.run_until_complete(handler.wait_closed())
loop.run_until_complete(loop.shutdown_asyncgens())
loop.close()

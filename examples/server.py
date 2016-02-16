import engineio
from gevent import pywsgi

import logging
logging.basicConfig(level=logging.DEBUG)

eio = engineio.Server()

@eio.on('message')
def message(sid, msg):
    eio.send(sid, "Server received: %s"%msg)

app = engineio.Middleware(eio)
pywsgi.WSGIServer(('', 8000), app).serve_forever()

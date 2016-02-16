from engineio_client.client import Client

import gevent
import gevent.monkey
gevent.monkey.patch_all()

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

eio = Client('localhost', 8000)

@eio.on('open')
def on_open():
    eio.send("Hello")

@eio.on('message')
def on_message(message):
    print message
    eio.close()

eio.open()
gevent.wait()

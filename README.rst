python-engineio-client
======================

Python implementation of the engine.io client.

Design & goals
--------------

This implementation is inspired by the JavaScript `engine.io-client`_
implementation.

Protocol parser is copied in parts and at least largely inspired from the
package `python-engineio`_ written by `Miguel Grinberg`_.

This engine.io client is using `Gevent`_ for now. This is not a strict design
choice but a simplification for this first implementaion. Other asynchronous
frameworks are welcome for future versions.

Example
-------

::

    from engineio_client.client import Client

    import gevent
    import gevent.monkey
    gevent.monkey.patch_all()

    eio = Client('localhost', 8000)

    @eio.on('message')
    def on_message(message):
        print message
        eio.close()

    @eio.on('open')
    def on_open():
        eio.send("Hello")

    eio.open()
    gevent.wait()


Links
-----

Another engine.io/socket.io client: `socketIO_client`_

.. _engine.io-client: https://github.com/socketio/engine.io-client
.. _python-engineio: https://github.com/miguelgrinberg/python-engineio
.. _Miguel Grinberg: https://github.com/miguelgrinberg
.. _gevent: http://gevent.org/
.. _socketIO_client: https://github.com/invisibleroads/socketIO-client

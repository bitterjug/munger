import threading
import tornado
from .application import Application


ioloop = tornado.ioloop.IOLoop.instance()


def start(TESTING_PORT = 8192):
    """ Start Application runing on given port """
    app = Application()
    app.listen(TESTING_PORT)
    thread = threading.Thread(target=ioloop.start)
    thread.start()
    return thread


def stop(thread):
    """ Ask IOLoop to stop running, and wait for its thread to complete"""
    ioloop.add_callback(ioloop.stop)
    thread.join()

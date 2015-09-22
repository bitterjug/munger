import signal
import tornado.ioloop

from webapp.application import Application

ioloop = tornado.ioloop.IOLoop.instance()


def signal_handler(signum, frame):
    ioloop.add_callback_from_signal(ioloop.stop)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    Application().listen(8888)
    ioloop.start()


if __name__ == "__main__":
    main()

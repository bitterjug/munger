import tornado.ioloop
from webapp.application import Application


def main():
    Application().listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1>Munger</h1>")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        tornado.web.Application.__init__(self, handlers)
